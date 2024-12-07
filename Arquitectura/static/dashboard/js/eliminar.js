function eliminarUsuario(id) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "¡Sí!",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "¡Usuario eliminado!",
                text: "El usuario ha sido eliminado.",
                icon: "success"
            }).then(() => {
                window.location.href = "/dashboard/usuarios/eliminar/" + id;
            });
        }
    });
};

function eliminarProducto(id) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "¡Sí!",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "¡Producto eliminado!",
                text: "El producto ha sido eliminado.",
                icon: "success"
            }).then(() => {
                window.location.href = "/dashboard/productos/eliminar/" + id;
            });
        }
    });
}

function eliminarVehiculo(id) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "¡Sí!",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "¡Vehículo eliminado!",
                text: "El vehículo ha sido eliminado.",
                icon: "success"
            }).then(() => {
                window.location.href = "/dashboard/vehiculos/eliminar/" + id;
            });
        }
    });
};

function eliminarVenta(id) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "¡Sí!",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Venta eliminada!",
                text: "La venta ha sido eliminada.",
                icon: "success"
            }).then(() => {
                window.location.href = "/dashboard/ventas/eliminar/" + id;
            });
        }
    });
}