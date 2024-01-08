let dataTable;
let dataTableIsInitialized=false;

const dataTableOptions ={
    columnDefs:[
        {classname: "centered", targets:[0,1,2,3,4,5,6,7,8,9]},
        {orderable: true, targets:[0,1,2,3,4,5,6,7,8,9]},
        {searchable: true, targets:[0,1,2,3,4,5,6,7,8,9]} 
    ]
}

const initDataTable=async() =>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await encuesta();

    dataTable=$('#dataTables-example').DataTable(dataTableOptions);
    dataTableIsInitialized = true
};

const encuesta = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/encuesta/", { mode: 'no-cors' });
        const data = await response.json();

        let content = '';
        data.encuesta.forEach((encuesta, index) => {
            content += `
                <tr>
                    <td>${encuesta.precios}</td>
                    <td>${encuesta.empanadas}</td>
                    <td>${encuesta.cortes}</td>
                    <td>${encuesta.guarniciones}</td>
                    <td>${encuesta.postres}</td>
                    <td>${encuesta.salsapastas}</td>
                    <td>${encuesta.alcohol}</td>
                    <td>${encuesta.cervezas}</td>
                    <td>${encuesta.refrescos}</td>
                    <td>${encuesta.cafes}</td>
                </tr>
            `;
        });

        tableBody_encuestas.innerHTML = content;

    } catch (ex) {
        alert(ex);
    }
};
window.addEventListener("load", async() => {
    await initDataTable();
});