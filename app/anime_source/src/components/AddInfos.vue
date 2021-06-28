<template
  ><main
    class="profile-page"
    style="weight: 80%;"
    v-if="id != null && isLoaded != false"
  >
    <section class="relative py-16" v-if="studios != null">
      <div class="container mx-auto px-4">
        <h3 class="text-xl font-bold block text-clack">
          More Information
        </h3>
        <div>
          <div
            class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-5"
          >
            <div class="rounded overflow-hidden shadow-lg">
              <label class="text-xl font-bold text-yellow-600">
                Studios:
              </label>
              <br />
              <br />
              <div
                class="bg-yellow-50 mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                v-for="item in studios"
                :key="item"
              >
                <div class="sm:flex sm:items-center px-6 py-4">
                  <img
                    class="block h-16 sm:h-14 md:h-14 md:max-h-10 rounded-2xl mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                    :src="item.photo"
                    alt=""
                  />
                  <div class="text-center sm:text-left sm:flex-grow">
                    <div class="mb-4">
                      <p class="text-xl leading-tight">{{ item.title }}</p>
                    </div>
                    <div>
                      <a
                        :href="'/studios/' + item.id"
                        class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-yellow-500"
                      >
                        More
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="rounded overflow-hidden shadow-lg">
              <label class="text-xl font-bold text-yellow-600">
                Producers:
              </label>
              <br />
              <br />
              <div v-for="item in producers" :key="item">
                <div
                  class="bg-yellow-50 mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                >
                  <div class="sm:flex sm:items-center px-6 py-4">
                    <img
                      class="block h-16 sm:h-14 md:h-16 rounded-2xl mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                      :src="item.photo"
                      alt=""
                    />
                    <div class="text-center sm:text-left sm:flex-grow">
                      <div class="mb-4">
                        <p class="text-xl leading-tight">{{ item.title }}</p>
                      </div>
                      <div>
                        <a
                          :href="'/producers/' + item.id"
                          class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-yellow-500"
                        >
                          More
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
                <br />
              </div>
            </div>
            <div class="rounded overflow-hidden shadow-lg">
              <label class="text-xl font-bold text-yellow-600">
                Licenses:
              </label>
              <br />
              <br />
              <div v-for="item in licencers" :key="item">
                <div
                  class="bg-yellow-50 mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                >
                  <div class="sm:flex sm:items-center px-6 py-4">
                    <img
                      class="block h-20 sm:h-15 rounded-2xl mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                      src="https://civicwise.com/wp-content/uploads/elementor/thumbs/CivicWise-Icon-Business-License-400x400-1-onyyrm623xjdsf7lgt64rgwnycl064hjcspukcxcq0.png"
                      alt=""
                    />
                    <div class="text-center sm:text-left sm:flex-grow">
                      <p class="text-xl leading-tight">{{ item.title }}</p>

                      <div></div>
                    </div>
                  </div>
                </div>
                <br />
              </div>
            </div>
          </div>
        </div>
        <div class="p-10 grid gap-5">
          <div class="rounded overflow-hidden shadow-lg">
            <label class="text-xl font-bold text-yellow-600">
              Themes:
            </label>

            <br />
            <br />
            <div v-for="item in themes" :key="item">
              <div
                class="bg-yellow-50 mx-auto ml-5 mr-5 shadow-lg rounded-lg overflow-hidden"
              >
                <div class="inline-flex items-center px-6 py-4">
                  <img
                    class="block h-20 sm:h-15 rounded-2xl mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                    src="https://img.icons8.com/bubbles/452/youtube-music.png"
                    alt=""
                  />
                  <div class="text-center sm:text-left sm:flex-grow">
                    <p class="text-xl leading-tight">{{ item.title }}</p>
                    <p class="leading-tight text-md text-gray-600">
                      {{ item.artist }}
                    </p>
                    <div></div>
                  </div>
                </div>
              </div>
              <br />
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
<script>
var gdb = require("../utils/graphdb");
var axios = require("axios");
export default {
  name: "AddInfos",
  props: {
    id: String,
  },
  data() {
    return {
      isLoaded: false,
      producers: [],
      themes: [],
      licencers: [],
      studios: [],
    };
  },
  async created() {
    var qThemes =
      `select * where {
        :anime_` +
      this.id +
      ` ?i :Anime;
           :hasTheme  ?ep.
           ?ep :title ?l;
               :artist ?a

            }`;
    var qStudios =
      `select * where {
        :anime_` +
      this.id +
      ` ?i :Anime;
           :hasStudio  ?ep.
           ?ep :name ?l;

            } `;
    var qProducers =
      `select * where {
        :anime_` +
      this.id +
      ` ?i :Anime;
           :hasProducer ?ep.
           ?ep :name ?l;

            } `;
    var qLicencers =
      `select * where {
        :anime_` +
      this.id +
      ` ?i :Anime;
           :hasLicense ?ep.
           ?ep :name ?l;

            }`;
    const h = gdb
      .fetchOntobud(qThemes)
      .then(async (response) => {
        this.themes = response.data.results.bindings.map((el) => {
          return {
            artist: el.a.value,
            title: el.l.value,
            id: el.ep.value.split("#")[1].split("_")[1],
          };
        });
      })
      .catch((e) => console.log(e));
    const i = gdb
      .fetchOntobud(qProducers)
      .then(async (response) => {
        response.data.results.bindings.map(async (el) => {
          axios
            .get(
              "https://www.googleapis.com/customsearch/v1?key=" +
                process.env.VUE_APP_KEY +
                "&cx=b4564266b17feb682&searchType=image&q=" +
                el.l.value +
                "+Producer+logo"
            )
            .then((j) => {
              this.producers.push({
                photo: j.data.items[0].link,
                title: el.l.value,
                id: el.ep.value.split("#")[1].split("_")[1],
              });
            })
            .catch(() => {
              this.producers.push({
                photo:
                  "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                title: el.l.value,
                id: el.ep.value.split("#")[1].split("_")[1],
              });
            });
        });
      })
      .catch((e) => console.log(e));
    const j = gdb
      .fetchOntobud(qStudios)
      .then(async (response) => {
        response.data.results.bindings.map(async (el) => {
          axios
            .get(
              "https://www.googleapis.com/customsearch/v1?key=" +
                process.env.VUE_APP_KEY +
                "&cx=b4564266b17feb682&searchType=image&q=" +
                el.l.value +
                "+Studio+logo"
            )
            .then((j) => {
              this.studios.push({
                photo: j.data.items[0].link,
                title: el.l.value,
                id: el.ep.value.split("#")[1].split("_")[1],
              });
            })
            .catch(() => {
              this.studios.push({
                photo:
                  "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                title: el.l.value,
                id: el.ep.value.split("#")[1].split("_")[1],
              });
            });
        });
        console.log(this.studios);
      })
      .catch((e) => console.log(e));
    const k = gdb
      .fetchOntobud(qLicencers)
      .then(async (response) => {
        response.data.results.bindings.map((el) => {
          this.licencers.push({
            title: el.l.value,
          });
        });
        console.log(this.licencers);
      })
      .catch((e) => console.log(e));
    await Promise.resolve(h);
    await Promise.resolve(i);
    await Promise.resolve(j);
    await Promise.resolve(k);
    this.isLoaded = true;
    console.log("istrue");
  },
};
</script>
