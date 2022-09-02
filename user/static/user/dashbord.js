
htmx.on("appoitment_delete", function (e){
    let number_appointments = document.querySelector("#number_appointments")
    let appointmen_content = document.querySelector("#appointmen_content")
    
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 2000,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })
    Toast.fire({
        icon: 'success',
        title: 'Rendez-vous supprimé'
    })

    number_appointments.innerHTML = e.detail.number_appointment

    appointmen_content.innerHTML = ""
    
});

htmx.on("service_delete", function (e){
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 2000,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })
    Toast.fire({
        icon: 'success',
        title: 'Service supprimé'
    })
});
