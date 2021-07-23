
const MAIN_STORE = `process.env[process.platform == "win32" ? "USERPROFILE" : "HOME"]/${'.pds'}`;

const MAIN_DB = `${MAIN_STORE}/main.db`;
