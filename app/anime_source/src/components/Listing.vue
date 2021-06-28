<template>
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
              v-if="tipe != 'Search' && tipe != 'Genre'"
              :to="{ name: tipe, params: { id: item.id } }"
              class="font-bold text-xl mb-2"
              >{{ item.nome }}</router-link
            >
            <router-link
              v-if="tipe == 'Search' || tipe == 'Genre'"
              :to="{ name: 'Anime', params: { id: item.id } }"
              class="font-bold text-xl mb-2"
              >{{ item.nome }}</router-link
            >
            <p class="text-gray-700 text-base">
              {{ item.type }}
            </p>
            <p class="text-gray-700 text-xs">
              {{ item.status }}
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >{{ item.NAnimes }}</span
            >
            <span
              class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >{{ item.favs }}</span
            >
            <span
              class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >{{ item.tag }}</span
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
</template>

<script>
import VueTailwindPagination from "./Pagination.vue";
var gdb = require("../utils/graphdb");
var axios = require("axios");
export default {
  components: {
    VueTailwindPagination,
  },
  props: {
    tipe: String,
    result: String,
  },
  data() {
    return {
      producers: null,
      currentPage: 1,
      perPage: 3,
      header: "https://wallpapercave.com/wp/wp4712029.jpg",
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
      var query = "";
      this.currentPage = currentPage;
      if (this.tipe == "Anime") {
        query = ` select * where {
        ?anime ?s :Anime;
             :favorites ?i;
    :title ?name;
    :episodes ?e;
    :status ?sd;
    :favorites ?f;
    :premiered ?pr;
    :type ?t;
    }   order by DESC(?i)`;
      } else if (this.tipe == "Search") {
        query =
          `select * where {
	?anime ?p :Anime ;
    :favorites ?i;
    :episodes ?e;
    :status ?sd;
    :favorites ?f;
    :premiered ?pr;
    :type ?t;
    :title ?name.
    OPTIONAL {
        ?anime ?p :Anime ;
        :title_japanese ?nameJapanese;
   	}
    OPTIONAL {
        ?anime ?p :Anime ;
        :title_english ?nameEnglish;
    }

    FILTER (
        regex( lcase(str(?name)), lcase("` +
          this.result +
          `")) ||
        regex( lcase(str(?nameJapanese)), lcase("` +
          this.result +
          `")) ||
        regex( lcase(str(?nameEnglish)), lcase("` +
          this.result +
          `")) ||
        regex( lcase(str(?nameSynonyms)), lcase("` +
          this.result +
          `"))
            )
} order by DESC(?i)`;
      } else if (this.tipe == "Genre") {
        query =
          `select * where {
        ?anime ?s :Anime;
             :favorites ?i;
    :title ?name;
    :episodes ?e;
    :status ?sd;
    :favorites ?f;
    :premiered ?pr;
    :type ?t;
    :has` +
          this.tipe +
          ` :genre_` +
          this.result +
          `.
    }   order by DESC(?i)`;
      } else {
        query =
          `
    select (count(?anime) as ?NAnimes ) ?producer ?nome  where {
        ?anime ?s :Anime;
             :has` +
          this.tipe +
          ` ?producer.
        ?producer :name ?nome.
    } group by ?producer ?nome
      order by DESC(?NAnimes)
    `;
      }
      gdb
        .fetchOntobud(query)
        .then(async (response) => {
          this.total = response.data.results.bindings.length;

          var i = 0;
          while (i < 3) {
            var d =
              response.data.results.bindings[
                (this.currentPage - 1) * this.perPage + i
              ];
            var nome = "";
            var amostra = "";
            var coiso = "";
            var se = "";
            if (
              this.tipe == "Anime" ||
              this.tipe == "Search" ||
              this.tipe == "Genre"
            ) {
              nome = d.name.value.replace(" ", "+");
              amostra = "cover";
              coiso = "" + amostra;
              se = 1;
            } else {
              nome = d.nome.value.replace(" ", "+");
              amostra = "logo";
              coiso = this.tipe + "+" + amostra;
              se = 0;
            }
            const p = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=" +
                  process.env.VUE_APP_KEY +
                  "&cx=b4564266b17feb682&searchType=image&q=" +
                  nome +
                  "+" +
                  coiso
              )
              .then((dat) => {
                if (
                  this.tipe == "Anime" ||
                  this.tipe == "Search" ||
                  this.tipe == "Genre"
                ) {
                  this.producers.push({
                    id: d.anime.value.split("#")[1].split("_")[1],
                    NAnimes: d.e.value + " Episodes",
                    nome: d.name.value,
                    photo: dat.data.items[se].link,
                    status: d.sd.value,
                    type: d.t.value,
                    favs: d.f.value + " 💛",
                    tag: d.pr.value,
                  });
                } else {
                  this.producers.push({
                    id: d.producer.value.split("#")[1].split("_")[1],
                    NAnimes: d.NAnimes.value + " Animes",
                    nome: d.nome.value,
                    photo: dat.data.items[se].link,
                    status: "",
                    type: "",
                    favs: " 📝 ",
                    tag: " 🏢 ",
                  });
                }
              })
              .catch(() => {
                if (
                  this.tipe == "Anime" ||
                  this.tipe == "Search" ||
                  this.tipe == "Genre"
                ) {
                  this.producers.push({
                    id: d.anime.value.split("#")[1].split("_")[1],
                    NAnimes: d.e.value + " Episodes",
                    nome: d.name.value,
                    photo:
                      "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                    status: d.sd.value,
                    type: d.t.value,
                    favs: d.f.value + " 💛",
                    tag: d.pr.value,
                  });
                } else {
                  this.producers.push({
                    id: d.producer.value.split("#")[1].split("_")[1],
                    NAnimes: d.NAnimes.value + " Animes",
                    nome: d.nome.value,
                    status: "",
                    type: "",
                    favs: " 📝 ",
                    tag: " 🏢 ",
                    photo:
                      "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                  });
                }
              });
            await Promise.resolve(p);
            i = i + 1;
          }
        })
        .catch((e) => {
          console.log("Erro no get producers " + e);
        });
    },
  },
};
</script>
