function deleteUser(userId) {
    fetch("/delete_user/" + userId, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            if (data.success) {
                location.reload();
            } else {
                console.error("Deletion failed:", data.error);
            }
        })
        .catch((error) => {
            console.error("There was an error!", error);
        });
}