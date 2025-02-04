// Funció per llegir el CSV
async function llegirCSV() {
    const response = await fetch('resultado_estadistica.csv'); // Ruta al teu CSV
    const data = await response.text();
    return data;
}

// Funció per convertir el CSV en un array d'objectes
function parsejarCSV(csv) {
    const linies = csv.split('\n');
    const resultat = [];
    const capçaleres = linies[0].split(',');

    for (let i = 1; i < linies.length; i++) {
        const obj = {};
        const currentLine = linies[i].split(',');

        for (let j = 0; j < capçaleres.length; j++) {
            obj[capçaleres[j]] = currentLine[j];
        }
        resultat.push(obj);
    }
    return resultat;
}

// Funció per crear la gràfica de variació anual
function crearGraficaVariacio(dades) {
    const ctx = document.getElementById('grafica1').getContext('2d');
    const labels = dades.map(entry => entry.Mes); // Extraure els mesos
    const vendes = dades.map(entry => parseInt(entry.Vendes)); // Extraure les vendes

    new Chart(ctx, {
        type: 'line', // Tipus de gràfica
        data: {
            labels: labels,
            datasets: [{
                label: 'Variació Anual',
                data: vendes,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Funció per crear la gràfica de mitjanes
function crearGraficaMitjanes(dades) {
    const ctx = document.getElementById('grafica2').getContext('2d');
    const labels = dades.map(entry => entry.Mes); // Extraure els mesos
    const vendes = dades.map(entry => parseInt(entry.Vendes)); // Extraure les vendes

    const totalVendes = vendes.reduce((a, b) => a + b, 0);
    const mitjanaVendes = totalVendes / vendes.length;

    new Chart(ctx, {
        type: 'bar', // Tipus de gràfica
        data: {
            labels: labels,
            datasets: [{
                label: 'Mitjanes Mensuals',
                data: vendes.map(() => mitjanaVendes),
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Funció per crear la gràfica d'extrems
function crearGraficaExtrems(dades) {
    const ctx = document.getElementById('grafica3').getContext('2d');
    const labels = dades.map(entry => entry.Mes); // Extraure els mesos
    const vendes = dades.map(entry => parseInt(entry.Vendes)); // Extraure les vendes

    const maximaVenda = Math.max(...vendes);
    const minimaVenda = Math.min(...vendes);

    new Chart(ctx, {
        type: 'bar', // Tipus de gràfica
        data: {
            labels: labels,
            datasets: [{
                label: 'Extrems de Vendes',
                data: vendes,
                backgroundColor: vendes.map(venda => venda === maximaVenda ? 'rgba(255, 99, 132, 0.2)' : (venda === minimaVenda ? 'rgba(54, 162, 235, 0.2)' : 'rgba(75, 192, 192, 0.2)')),
                borderColor: vendes.map(venda => venda === maximaVenda ? 'rgba(255, 99, 132, 1)' : (venda === minimaVenda ? 'rgba(54, 162, 235, 1)' : 'rgba(75, 192, 192, 1)')),
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Funció principal
async function main() {
    const csv = await llegirCSV();
    document.getElementById('csv-data').textContent = csv; // Mostrar el CSV en pantalla
    const dades = parsejarCSV(csv);

    crearGraficaVariacio(dades); // Crear la gràfica de variació anual
    crearGraficaMitjanes(dades); // Crear la gràfica de mitjanes
    crearGraficaExtrems(dades); // Crear la gràfica d'extrems
}

// Executar la funció principal
main();
