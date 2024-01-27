
function salir(){
  window.location ="/../login.html";
}
function imprimir() {
  // Captura la página con html2canvas
  html2canvas(document.body, { scale: 2 }).then(function(canvas) {
    // Convierte el canvas a imagen base64
    var imgData = canvas.toDataURL('image/png');

    // Crea un objeto jsPDF con tamaño carta (8.5 x 11 pulgadas)
    var pdf = new jsPDF('p', 'in', [8.5, 11]);

    // Calcula el ancho y alto de la imagen para adaptarse a la página
    var imgWidth = pdf.internal.pageSize.width;
    var imgHeight = (canvas.height * imgWidth) / canvas.width;

    // Agrega la imagen al PDF
    pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);

    // Descarga el PDF
    pdf.save('captura.pdf');
  });
}