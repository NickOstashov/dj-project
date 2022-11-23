
let coll = document.getElementsByClassName("collapse-bt")
for (let i =0; i<coll.length;i++){
    coll[i].addEventListener('click',function(){
        this.classList.toggle('active');
        let contant = this.nextElementSibling;
        if (contant.style.maxHeight){
            contant.style.maxHeight = null;
        } else {
            contant.style.maxHeight = contant.scrollHeight + "px"
        }
    })
}