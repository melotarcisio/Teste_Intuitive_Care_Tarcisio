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
            <div v-for="comment in search_" id="p_result">
                <h1>{{ comment.result1 }}</h1>
            </div>
        </div>
    `,
    data() {
        return {
            search_:[{
                result1: '',
            }],
            pesquisa: '',
        }
    },
    methods:{
        async newSearch(){
            if(this.pesquisa.trim()=== ''){return}
            console.log(this.pesquisa),
            await axios
            .get("http://localhost:8088/search",{'headers':{'src':this.pesquisa}})
            .then(response => (this.info = response))
            .catch(),
            console.log(this.info),
            r = JSON.parse(JSON.stringify(this.info['data'])),
            this.search_.push({
                result1:'Razão Social: ' + r['r1']['Razão Social'] + ',
                    CNPJ: '+ r['r1']['CNPJ'] + ',
                    Registro ANS: ' + r['r1']['Registro ANS'],
                    'Razão Social: ' + r['r2']['Razão Social'] + ',
                    CNPJ: '+ r['r2']['CNPJ'] + ',
                    Registro ANS: ' + r['r2']['Registro ANS'],
                    'Razão Social: ' + r['r3']['Razão Social'] + ',
                    CNPJ: '+ r['r3']['CNPJ'] + ',
                    Registro ANS: ' + r['r3']['Registro ANS'],
            })
            this.pesquisa = ''
        }
    }   
})
