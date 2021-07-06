const app = Vue.createApp({
    data() {
        return {
            vm: {
                currentTime: "ボタンを押すとここに現在時刻が表示されます",
                dailyProgress: undefined,
                yearlyProgress: undefined
            }
        }
    },
    mounted() {
        // タイマー処理（別途関数にしないと正常に動作しない）
        window.setInterval(() => eel.server_get_time_progress(), 1000);
    },
    methods: {
        updateMessage(newViewModel){
            this.vm = newViewModel;
        }
    }
}).mount("#app");

// Eelで公開する関数（公開名を指定）
eel.expose(app.updateMessage, "client_updateMessage");
