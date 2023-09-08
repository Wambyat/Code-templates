const axios = require("axios");

// axios secion

// GET
axios
    .get(url)
    .then((response) => {
        const res = response.data;
    })
    .catch((error) => {
        console.log(error);
    });

// POST
data = {
    name: "John Doe",
    age: 25,
};
axios
    .post(url, data)
    .then((response) => {
        const res = response.data;
    })
    .catch((error) => {
        console.log(error);
    });

// with headers
data = {
    name: "John Doe",
    age: 25,
};
const config = {
    headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
    },
};
axios
    .post(url, data, config)
    .then((response) => {
        const res = response.data;
    })
    .catch((error) => {
        console.log(error);
    });

// Using fetch

// GET
fetch(url)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    });

// POST
data = {
    name: "John Doe",
    age: 25,
};
fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        "Content-Type": "application/json",
    },
})
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    });
