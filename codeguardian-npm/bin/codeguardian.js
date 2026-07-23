#!/usr/bin/env node

const { spawn } = require("child_process");

const args = process.argv.slice(2);

const child = spawn(
    "python3",
    [
        "-m",
        "CODEGUARDIAN.main",
        ...args
    ],
    {
        stdio: "inherit"
    }
);

child.on("exit", (code) => {

    process.exit(code);

});