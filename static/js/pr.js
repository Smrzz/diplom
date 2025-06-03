function openForm(formId) {
    const form = document.getElementById(formId);
    form.style.display = "block";
    
   
    form.style.position = "fixed";
    form.style.top = "50%";
    form.style.left = "50%";
    form.style.transform = "translate(-50%, -50%)";
    

    setTimeout(() => {
        document.addEventListener('click', closeFormOnClickOutside);
    }, 0); 
}

function closeForm(formId) {
    const form = document.getElementById(formId);
    form.style.display = "none";
    document.removeEventListener('click', closeFormOnClickOutside);
}

function closeFormOnClickOutside(e) {
    const forms = document.querySelectorAll('.form-popup');
    
    forms.forEach((form) => {
        if (form.style.display === "block" && !form.contains(e.target) && !e.target.closest('.btn-gast')) {
            form.style.display = "none"; 
        }
    });
}
