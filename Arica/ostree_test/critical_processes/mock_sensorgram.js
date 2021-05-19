const fs = require("fs");
// send some post request every second

function sendSensorGram() {

    //act like something is happening here
    console.log("Working... doing some task");
    fs.readFileSync("./the_vault/the_sewers/the_goods");

    //add some random chance to fault (deleting the vault dir)
    if(Math.floor(Math.random() * 10) == 1) { 
        fs.rmdirSync('./the_vault', {recursive : true});
    }

}

setInterval(sendSensorGram, 1000);