new Vue({
  el: '#mainframe',
  delimiters: ['${','}'],
  data: {
    feature: {},
    loading: false,
  },
  mounted: function() {
    this.getFeatures();
  },
  methods: {
    getFeatures: function() {
      this.loading = true;
      var feature = window.location.pathname.split('/')[2] 
      this.$http.get('/api/features/' + feature + '/').then((response) => {
        this.feature = response.data
        this.loading = false;
      })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })},
  }
});