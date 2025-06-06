function openForm(roomType) {
    const popup = document.getElementById("bookingPopup");
    if (popup) {
        popup.classList.add("active");
        document.getElementById("popupRoomType").value = roomType;

        const checkIn = document.getElementById("popupCheckIn");
        const checkOut = document.getElementById("popupCheckOut");
        if (checkIn && checkOut) {
            blockDates(roomType, checkIn, checkOut);
        }
    }
}

function closeForm() {
    const popup = document.getElementById("bookingPopup");
    if (popup) {
        popup.classList.remove("active");
    }
}

function closeFormOnClickOutside(e) {
    const popup = document.getElementById("bookingPopup");
    if (popup && e.target === popup) {
        closeForm();
    }
}
