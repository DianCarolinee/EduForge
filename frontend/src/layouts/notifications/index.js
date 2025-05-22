import React, { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import * as XLSX from "xlsx";
import { useNavigate } from "react-router-dom";

// @mui/material
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";

// Componentes del Dashboard
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";

// Layout
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

function UploadData() {
  const [fileData, setFileData] = useState([]);
  const [fileName, setFileName] = useState("");
  const [rawFile, setRawFile] = useState(null); // Guardamos el archivo original
  const [isProcessing, setIsProcessing] = useState(false);
  const [predictions, setPredictions] = useState([]);
  const navigate = useNavigate();
  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    setRawFile(file); // Guardamos el archivo original
    setFileName(file.name);

    const reader = new FileReader();
    reader.onload = (e) => {
      const data = new Uint8Array(e.target.result);
      const workbook = XLSX.read(data, { type: "array" });
      const worksheet = workbook.Sheets[workbook.SheetNames[0]];
      const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
      setFileData(json);
    };

    reader.readAsArrayBuffer(file);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: [".csv", ".xlsx", ".xls"],
  });

  const handleUpload = async () => {
    if (!rawFile) {
      alert("No hay archivo para enviar.");
      return;
    }
    setIsProcessing(true);

    try {
      // Paso 1: Subir el archivo
      const formData = new FormData();
      formData.append("file", rawFile);

      const uploadRes = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });

      if (!uploadRes.ok) {
        throw new Error("Error al subir el archivo");
      }
      const uploadResult = await uploadRes.json();
      // Paso 2: Procesar el archivo para predicciones
      const predictRes = await fetch(
        `http://localhost:8000/predict?filename=${encodeURIComponent(uploadResult.filename)}`,
        {
          method: "POST",
        }
      );
      if (!predictRes.ok) {
        throw new Error("Error al procesar el archivo");
      }

      const predictions = await predictRes.json();

      // Paso 3: Navegar a la página de resultados con los datos
      navigate("/billing", { state: { predictions: predictions.predictions } });
    } catch (error) {
      alert("Error al procesar el archivo");
      console.error(error);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox mt={6} mb={3}>
        <Grid container spacing={3} justifyContent="center">
          <Grid item xs={12} md={10}>
            <Card>
              <MDBox p={4}>
                <MDTypography variant="h5" mb={2}>
                  Subir archivo CSV o Excel para análisis
                </MDTypography>
                <MDBox
                  {...getRootProps()}
                  sx={{
                    border: "2px dashed #aaa",
                    borderRadius: "10px",
                    padding: "40px",
                    textAlign: "center",
                    backgroundColor: isDragActive ? "#f0f0f0" : "#fafafa",
                    cursor: "pointer",
                  }}
                >
                  <input {...getInputProps()} />
                  <Icon fontSize="large">cloud_upload</Icon>
                  <MDTypography variant="body1">
                    {isDragActive
                      ? "Suelta el archivo aquí..."
                      : "Arrastra y suelta un archivo aquí o haz clic para seleccionar"}
                  </MDTypography>
                </MDBox>

                {fileName && (
                  <MDBox mt={2}>
                    <MDTypography variant="subtitle1">
                      <strong>Archivo cargado:</strong> {fileName}
                    </MDTypography>
                  </MDBox>
                )}

                {fileData.length > 0 && (
                  <MDBox mt={4} maxHeight="300px" sx={{ overflow: "auto" }}>
                    <MDTypography variant="h6" mb={1}>
                      Vista previa:
                    </MDTypography>
                    <table style={{ width: "100%", borderCollapse: "collapse" }}>
                      <tbody>
                        {fileData.slice(0, 10).map((row, i) => (
                          <tr key={i}>
                            {row.map((cell, j) => (
                              <td
                                key={j}
                                style={{
                                  border: "1px solid #ddd",
                                  padding: "8px",
                                  fontSize: "14px",
                                }}
                              >
                                {cell}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </MDBox>
                )}

                <MDBox mt={4}>
                  <MDButton
                    variant="gradient"
                    color="info"
                    onClick={handleUpload}
                    disabled={!rawFile}
                  >
                    Enviar
                  </MDButton>
                </MDBox>

                {predictions.length > 0 && (
                  <MDBox mt={4}>
                    <MDTypography variant="h6" mb={1}>
                      Resultados de deserción:
                    </MDTypography>
                    <table style={{ width: "100%", borderCollapse: "collapse" }}>
                      <thead>
                        <tr>
                          {Object.keys(predictions[0]).map((col, i) => (
                            <th key={i} style={{ border: "1px solid #ccc", padding: "6px" }}>
                              {col}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {predictions.map((row, i) => (
                          <tr key={i}>
                            {Object.values(row).map((val, j) => (
                              <td key={j} style={{ border: "1px solid #ccc", padding: "6px" }}>
                                {val}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </MDBox>
                )}
              </MDBox>
            </Card>
          </Grid>
        </Grid>
      </MDBox>
      <Footer />
    </DashboardLayout>
  );
}

export default UploadData;
