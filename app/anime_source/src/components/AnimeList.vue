<template>
    <div>
      <table class="table-fixed">
        <tr>
          <th>Nome</th>
          <th>Score</th>
          <th>Scored_by</th>
          <th>Rank</th>
          <th>status</th>
        </tr>
        <tr class="bg-emerald-200" v-for="anime in animes" :key="anime">
          <th>{{anime.nome}}</th>
          <th>{{anime.score}}</th>
          <th>{{anime.scored_by}}</th>
          <th>{{anime.rank}}</th>
          <th>{{anime.status}}</th>
        </tr>
      </table>
    </div>
</template>

<script>
var gdb = require("../utils/graphdb");
export default {
    data(){
        return {
            animes: [],
            currentPage: 1
        }
    },
    created(){
      this.list(1)
    },
    methods: {
      list: function (currentPage) {
      this.animes = [];
      this.currentPage = currentPage;
      var query = `
select ?anime ?nome ?status ?score ?scored_by ?rank where { 
	?anime a :Anime ;
     		:title ?nome ;
       		:status ?status ; 
         	:score ?score ;
          	:scored_by ?scored_by ;
          	:rank ?rank .
} order by DESC(?rank)
    `;

      gdb
        .fetchOntobud(query)
        .then(async (response) => {
          this.total = response.data.results.bindings.length;

          var i = 0;
          while (i < this.total) {
            var d = response.data.results.bindings[i];
            this.animes.push({
              nome: d.nome.value,
              status: d.status.value,
              score: d.score.value,
              scored_by: d.scored_by.value,
              rank: d.rank.value
            })
            i = i + 1;
          }

          console.log(this.animes);
        })
        .catch((e) => {
          console.log("Erro no get animes " + e);
        });
    },
    }


}
</script>
