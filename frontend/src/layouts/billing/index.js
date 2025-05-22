/**
=========================================================
* Material Dashboard 2 React - v2.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import React from "react";
import { useLocation } from "react-router-dom";

// @mui/material imports
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

function Billing() {
  const location = useLocation();
  const { predictions } = location.state || { predictions: [] };

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox mt={6} mb={3}>
        <Grid container spacing={3} justifyContent="center">
          <Grid item xs={12} md={10}>
            <Card>
              <MDBox p={4}>
                <MDTypography variant="h5" mb={2}>
                  Resultados de Predicción de Deserción
                </MDTypography>
                {predictions.length > 0 ? (
                  <MDBox mt={4} maxHeight="500px" sx={{ overflow: "auto" }}>
                    <table style={{ width: "100%", borderCollapse: "collapse" }}>
                      <thead>
                        <tr>
                          {Object.keys(predictions[0]).map((key) => (
                            <th
                              key={key}
                              style={{
                                border: "1px solid #ddd",
                                padding: "8px",
                                textAlign: "left",
                                backgroundColor: "#f2f2f2",
                              }}
                            >
                              {key}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {predictions.map((row, index) => (
                          <tr key={index}>
                            {Object.values(row).map((value, i) => (
                              <td
                                key={i}
                                style={{
                                  border: "1px solid #ddd",
                                  padding: "8px",
                                  backgroundColor:
                                    row.resultado === "Sí deserta" ? "#ffdddd" : "#ddffdd",
                                }}
                              >
                                {String(value)}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </MDBox>
                ) : (
                  <MDTypography variant="body1" color="error">
                    No hay datos de predicción disponibles.
                  </MDTypography>
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

export default Billing;
