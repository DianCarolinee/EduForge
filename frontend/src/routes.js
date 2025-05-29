import Dashboard from "layouts/dashboard";
import Tables from "layouts/tables";
import Billing from "layouts/billing";
import RTL from "layouts/rtl";
import Notifications from "layouts/notifications";
import Profile from "layouts/profile";
import SignIn from "layouts/authentication/sign-in";
import SignUp from "layouts/authentication/sign-up";

// @mui icons
import Icon from "@mui/material/Icon";

const routes = [
  {
    type: "collapse",
    name: "Reporte general",
    key: "dashboard",
    icon: <Icon fontSize="small">Reporte General</Icon>,
    route: "/reporte",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Análisis individual",
    key: "billing",
    icon: <Icon fontSize="small">receipt_long</Icon>,
    route: "/Analisis",
    component: <Billing />,
  },
  {
    type: "collapse",
    name: "Carga de datos",
    key: "notifications",
    icon: <Icon fontSize="small">notifications</Icon>,
    route: "/subir-archivos",
    component: <Notifications />,
  },
];

export default routes;
