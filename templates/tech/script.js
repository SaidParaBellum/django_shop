function changeLimit(select) {
        let limit = select.value;
        let currentPage = 1;
        let url = "{% url 'index' %}?page=" + currentPage + "&limit=" + limit;
        window.location.href = url;
    }