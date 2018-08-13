new Vue({
  el: '#mainframe',
  delimiters: ['${','}'],
  data: {
    features: [],
    loading: false,
    newFeature: {},
    message: null,
  },
  mounted: function() {
    this.getFeatures();
  },
  methods: {
    getFeatures: function() {
      this.loading = true;
      this.$http.get('/api/features/').then((response) => {
        this.features = response.data['objects'];
        this.loading = false;
      })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })},
    createFeature: function() {
      this.loading = true;
      console.log('hereeeeee')
      console.log(this.newFeature)
      //this.$http.post('/api/features/', this.newFeature)
    .then((response) => {
      this.loading = false;
      this.getFeatures();
    })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })},
  }
});