new Vue({
    el: "#starting",
    delimiters: ["${", "}"],
    data: {
        loading: false,
        newFeature: {
        },
    },
    mounted: function() {
    },
    methods: {
        addFeature: function() {
            this.loading = true;
            this.$http.post('/api/features/', this.newFeature)
                .then((response) => {
                    this.loading = false;
                    window.location.href = '/'
                })
                .catch((err) => {
                    this.loading = false;
                    //console.log(err)
                })

            }
    }
})