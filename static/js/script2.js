// script2.js
function DeleteRow(button) {
    // Find the row to be deleted
    var row = button.parentNode.parentNode;
    // Remove the row from the table
    row.parentNode.removeChild(row);
}
