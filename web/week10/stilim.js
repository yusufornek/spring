function bosGecilemez() {
    let x = document.forms["formum"]["f_ad"].value;
    if (x == "") {
        alert("Bu alan boş geçilemez! Lütfen uygun biçimde doldurunuz.");
        return false;
    }   
}