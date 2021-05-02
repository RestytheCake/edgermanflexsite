let createNewButtonPressed = false;

function newPostUsers(){
    let newPost = document.getElementById('createPost')

    if(createNewButtonPressed === false){
        newPost.style.display = 'block'
        createNewButtonPressed = true
    }else{
        newPost.style.display = 'none'
        createNewButtonPressed = false
    }
}