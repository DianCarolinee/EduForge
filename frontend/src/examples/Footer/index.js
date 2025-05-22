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
import Icon from "@mui/material/Icon";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React base styles
import typography from "assets/theme/base/typography";

function Footer() {
  const { size } = typography;

  return (
    <MDBox
      width="100%"
      display="flex"
      justifyContent="center"
      alignItems="center"
      px={1.5}
      py={2}
      color="text"
      fontSize={size.sm}
    >
      &copy; EduForge 2025, hecho con
      <MDBox fontSize={size.md} color="text" mb={-0.5} mx={0.25}>
        <Icon color="inherit" fontSize="inherit">
          favorite
        </Icon>
      </MDBox>
      para la educación y desarrollo académico
    </MDBox>
  );
}

export default Footer;
