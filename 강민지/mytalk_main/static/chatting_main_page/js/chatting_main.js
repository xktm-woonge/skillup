let side_bar_class = Array.from(document.getElementsByClassName('side_bar_detail'))
const GNB_bnt = Array.from(document.getElementsByClassName('icon_box'))

function hiddenSideBar(){
    side_bar_class.forEach(function(hsb){
        hsb.style.display = 'none';
    });
};

window.addEventListener('DOMContentLoaded', function(){
    hiddenSideBar();
    document.getElementById('able_login').style.display = 'block';
    document.getElementById('side_bar_notices').style.display = 'block';
});
GNB_bnt.forEach((clickbnt)=>{
    clickbnt.addEventListener('click',function(){
        let btnName = this.id.split('_')[0];
        hiddenSideBar();
        console.log(btnName);
        document.getElementById('side_bar_'+btnName).style.display = 'block';
        
    });
});
// document.getElementsByClassName('icon_box').addEventListener('click', function(){
    
//     
// });
