<template>
  <main class="profile-page">
    <Headerings :photo="header" :tipe="tipe" />
    <div>
      <div
        class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5"
      >
        <template v-for="item in producers" :key="item">
          <!--Card 1-->
          <div class="rounded overflow-hidden shadow-lg">
            <img
              class="object-contain h-48 w-full"
              :src="item.photo"
              alt="Mountain"
            />
            <div class="px-6 py-4">
              <router-link
                :to="{ name: 'Producer', params: { id: item.id } }"
                class="font-bold text-xl mb-2"
                >{{ item.nome }}</router-link
              >
              <p class="text-gray-700 text-base">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptatibus quia, nulla! Maiores et perferendis eaque,
                exercitationem praesentium nihil.
              </p>
            </div>
            <div class="px-6 pt-4 pb-2">
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#photography</span
              >
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#travel</span
              >
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#winter</span
              >
            </div>
          </div>
        </template>
      </div>
      <VueTailwindPagination
        :current="currentPage"
        :total="total"
        :per-page="perPage"
        @page-changed="
          current = $event;
          list(current);
        "
      />
    </div>
  </main>
</template>

<script>
var axios = require("axios");
import Headerings from "../components/Headerings.vue";
import VueTailwindPagination from "../components/Pagination.vue";
var gdb = require("../utils/graphdb");
export default {
  components: {
    Headerings: Headerings,
    VueTailwindPagination,
  },
  data() {
    return {
      producers: null,
      currentPage: 1,
      perPage: 3,
      header: "https://wallpapercave.com/wp/wp4712029.jpg",
      tipe: "Producers",
      title: this.producers,
      total: null,
    };
  },

  created() {
    this.list(1);
  },
  methods: {
    list: function (currentPage) {
      this.producers = [];
      this.currentPage = currentPage;
      var query = `
    select (count(?anime) as ?NAnimes ) ?producer ?nome  where {
        ?anime ?s :Anime;
             :hasProducer ?producer.
        ?producer :name ?nome.
    } group by ?producer ?nome
      order by DESC(?NAnimes)
    `;
      gdb
        .fetchOntobud(query)
        .then(async (response) => {
          console.log("response::: " + JSON.stringify(response));
          this.total = response.data.results.bindings.length;

          var i = 0;
          while (i < 3) {
            var d =
              response.data.results.bindings[
                (this.currentPage - 1) * this.perPage + i
              ];

            var nome = d.nome.value.replace(" ", "+");
            const p = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
                  nome +
                  "+producer+logo"
              )
              .then((dat) => {
                console.log("dat____:" + dat);
                console.log(d.producer.value.split("#")[1].split("_")[1]);
                this.producers.push({
                  id: d.producer.value.split("#")[1].split("_")[1],
                  NAnimes: d.NAnimes.value,
                  nome: d.nome.value,
                  photo: dat.data.items[0].link,
                });
              })
              .catch((e) => {
                console.log("Erro no get studios " + e);
                console.log(d);
                console.log(d.producer.value.split("#")[1].split("_")[1]);
                this.producers.push({
                  id: d.producer.value.split("#")[1].split("_")[1],
                  NAnimes: d.NAnimes.value,
                  nome: d.nome.value,
                  photo:
                    "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                });
              });
            await Promise.resolve(p);
            i = i + 1;
          }

          console.log(this.studios);
        })
        .catch((e) => {
          console.log("Erro no get producers " + e);
        });
    },
  },
};
</script>

<style></style>
