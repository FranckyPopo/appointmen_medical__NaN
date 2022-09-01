
htmx.on("appoitment_delete", function (e){
    let number_appointments = document.querySelector("#number_appointments")

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
});

htmx.on("htmx:afterOnLoad", function (e){
    let appointmen_content = document.querySelector(".email-body")
    let list_appointement = document.querySelectorAll(".contact-list-item")

    setTimeout(() => {
        if (list_appointement.length === 0){
            appointmen_content.innerHTML = "<h5>Vous avez aucun rendez-vous</h5>."
        }
        else {
            appointmen_content.innerHTML = "<h5>Cliquer sur en rendez-vous pour avoir plus de détail</h5>."
        }
    }, 250)

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
