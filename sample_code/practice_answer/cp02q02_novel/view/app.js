const app = Vue.createApp({
    data() {
        return {
            posts: []
        }
    },
    methods: {
        startLoading(event) {
            eel.server_load_novels();
        },
        updatePosts(newViewModel){
            this.posts = newViewModel;
        }
    }
}).mount("#app");

eel.expose(app.updatePosts, "client_updatePosts");
