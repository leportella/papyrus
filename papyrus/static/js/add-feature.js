new Vue({
    el: "#mainframe",
    delimiters: ["${", "}"],
    data: {
        loading: false,
        errors: [],
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
                    for (key in err.body.error) {
                        this.errors.push(key + ': ' +  err.body.error[key][0])
                    }
                    console.log(err)
                })
        }

    }
})
