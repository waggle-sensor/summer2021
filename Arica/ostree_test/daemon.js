const fs = require("fs");
const shell = require("shelljs");

// start our script for the first time

function checkForFault() { 

    //just check if the goods are intact
    if(!fs.existsSync("./the_vault/the_sewers/the_goods") ) { 
        console.log("Fault detected! Resetting....");
        //have OSTree reset the branch in another script
        shell.exec('./handle_fault.sh');

    }

}

setInterval(checkForFault, 500);