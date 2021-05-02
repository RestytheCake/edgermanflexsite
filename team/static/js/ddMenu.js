let profileClicked = false;

function ddMenu(){
    let ddcont = document.getElementById('dropdown-content');

    if(profileClicked === false){
        ddcont.style.display = 'block'
        profileClicked = true
    }else{
        ddcont.style.display = 'none'
        profileClicked = false
    }
}

/* This is Used from the Main Files / Where you have a Profile top Right */