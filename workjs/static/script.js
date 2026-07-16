document.addEventListener("DOMContentLoaded", async () => {

    try {

        const response = await fetch("/api/products");

        const products = await response.json();

        const table = document.getElementById("data");

        table.innerHTML = "";

        for (const p of products) {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${p.id}</td>
                <td>${p.name}</td>
                <td>₹${p.price}</td>
            `;

            table.appendChild(row);

        }

    }

    catch (error) {

        console.log(error);

    }

});