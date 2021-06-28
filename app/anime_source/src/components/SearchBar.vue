<template>
  <div class="flex flex-col items-center justify-center w-full bg-yellow-100">
    <span
      class="mb-3 font-semibold mt-3 text-yellow-700 text-xl px-2 text-center"
    >
      Search your favorite anime here!
    </span>
    <form
      @submit.prevent="
        this.$router.push({ name: 'Search', params: { id: input } })
      "
    >
      <div class="flex">
        <input
          type="text"
          name="anime"
          v-model.number="input"
          id="anime2"
          class="focus:ring-yellow-700 flex focus:border-yellow-600 pl-2 pr-2 sm:text-sm border-yellow-500 w-72 xl:w-120 md:w-96 lg:hidden rounded-md"
          placeholder="Search here..."
        />
        <button
          type="Submit"
          :href="'/search/' + input"
          class="bg-yellow-200 w-auto rounded-md flex lg:hidden left-8 items-center text-yellow-900 p-2 hover:text-yellows-400"
        >
          Search
        </button>
      </div>
    </form>
    <br />
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
    };
  },
};
</script>

<style></style>
