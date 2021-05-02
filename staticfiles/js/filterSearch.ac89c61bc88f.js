let filterClicked = false;

function filterSearch(){
    let filterList = document.getElementById('advancedList')
    let sortList = document.getElementById('sortList')

    if(filterClicked === false){
        filterList.style.display = 'block'
        sortList.style.display = 'block'
        filterClicked = true
    }else{
        filterList.style.display = 'none'
        sortList.style.display = 'none'
        filterClicked = false
    }
}