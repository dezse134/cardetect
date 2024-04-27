window.addEventListener('DOMContentLoaded', processImage);

function processImage() {
    const info = document.getElementById("fileinfo");

    const image_input = document.getElementById("image");
    image_input.addEventListener("change", updateFileInfo)

    function updateFileInfo() {
        while (info.firstChild) {
            info.removeChild(info.firstChild);
        }

        if (image_input.files.length === 0) {
            const para = document.createElement("p");
            para.textContent = "No fileinfo";
            info.appendChild(para);
            return
        }
        const file = image_input.files[0]

        const para = document.createElement("p");
        para.textContent = `Uploaded file name ${file.name}, file size ${file.size} bytes`
        info.appendChild(para);
        
        const image = document.createElement("img");
        image.src = URL.createObjectURL(file);
        image.alt = image.title = file.name;
        info.appendChild(image);
    }

    const query = new URLSearchParams(window.location.search)
    if (query.has('result')) {
        const image = document.createElement("img");
        const imageName = query.get('result')
        image.src = `/images/${imageName}`;
        image.alt = image.title = imageName;
        info.appendChild(image);
    }
}
