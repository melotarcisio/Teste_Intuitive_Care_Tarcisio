new Vue({
    el: '#app',
    template:`
        <div>
            <div id="cover">
                <div class="tb">
                    <div class="td">
                        <input type="text" name="src" v-model="pesquisa"><br>
                    </div>
                    <div class="td" id="s-cover">
                        <button v-on:click="newSearch" type="submit">
                            <div id="s-circle"></div>
                            <span></span>
                        </button>
                    </div>
                </div>
            </div>
            <div v-for="(comment,index) in search_" id="p_result">
                <h1>{{ comment.result1 }}</h1>
                <h1>{{ comment.result1 }}</h1>
                <h1>{{ comment.result1 }}</h1>
            </div>
        </div>
    `,
    data() {
        return {
            search_:[{
                result1: '',
                result2: '',
                result3: ''
            }],
            pesquisa: '',
        }
    },
    methods:{
        newSearch(){
            if(this.pesquisa.trim()=== ''){return}
            console.log('show'),
            console.log(this.pesquisa)
            this.search_.push({
                result1:this.pesquisa,
            })
            this.pesquisa = ''
        },
        mounted () {
            axios
            .get("http://8080-yellow-partridge-wflg6i6f.ws-us09.gitpod.io/search")
            .then(response => (this.info = response))
            console.log(this.info)
            }
    }   
})
