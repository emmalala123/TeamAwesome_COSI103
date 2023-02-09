
// ############# IMPORTS ####################
const { exit } = require('process');
var rl = require('readline-sync');

console.clear()

// #################################### MENU/CONSTRUCTORS #####################################################
 
/**
 * checking options for main menu
 * @param {*} value - 1 - 3
 */
let checkValue = value => {
    switch(value){
        case 1:
            console.clear()
            superSecret()
            break;
        case 2:
            process.exit()
        default:
            mainMenu()
            break;
    }
}

/**
 * initial directory listing
 */
let mainMenu = () => {
    let value = rl.question("stang -> press 1: \nquit -> press 2:\n")
    checkValue(+value)
}


mainMenu()


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
};
// // wait to print to console part 1
async function log(s, delay){
    await sleep(delay);
    process.stdout.write(s);
        
    process.stdout.write('\n');
};

function picPrint(pic, counter){
    for(var i in pic){
        log(pic[i], counter);
        counter += 30    
    }
}


// ######################################## SKIRT
// Artist => BLGM 
function superSecret(){
    var m = []
    m[0]="                      _--~~~~~~~~~~~~~~~~~~--_"
    m[1]="                    ./   ASCII MUSTANG ..      \\"
    m[2]="                  ./                            \\"
    m[3]="                (-.`., ~~~-----------------~~~-.,.-)"
    m[4]="                 / \\  - _ ,  {________} _. - - /  \\"
    m[5]="                /\\  . ____\\_           _/_____ .  /\\"
    m[6]="                |\\_/|____|_\\~_-_(@)_-_~/_|____|\\__/|"
    m[7]="                [  _____   /#         #\\  _____    ]"
    m[8]="                /.{ }...,,] \\ -- - -- / [,,.. { }. \\"
    m[9]="                \\--_((____)(___- - -___)(_____))_--/"
    m[10]="                |>>>>|        {83,50}         |<<<<|"
    m[11]="        ___   ` \\<<<>>>/'__"
    // @BLGM
    var counter = 60
    picPrint(m, counter)
    counter += 1000
    log(`\nVROOM!\n`, counter)
    counter += 1000
    setTimeout(mainMenu, counter)
}








  
           

            
            


