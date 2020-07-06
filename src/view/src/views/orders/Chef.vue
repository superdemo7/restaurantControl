<template>
  <div class="container is-fluid" style="display: grid; grid-template-columns: auto auto;">
    <div style="text-align: center; padding: 10%; margin: 10px;">
      <article class="panel is-info">
        <p class="panel-heading">Info</p>
        <p class="panel-tabs">
          <a class="is-active">All</a>
          <a>Public</a>
          <a>Private</a>
          <a>Sources</a>
          <a>Forks</a>
        </p>
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input is-info" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a class="panel-block is-active">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          bulma
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          marksheet
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          minireset.css
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          jgthms.github.io
        </a>
      </article>
    </div>
    <div>
      <article class="panel is-info">
        <p class="panel-heading">Info</p>
        <p class="panel-tabs">
          <a class="is-active">All</a>
          <a>Public</a>
          <a>Private</a>
          <a>Sources</a>
          <a>Forks</a>
        </p>
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input is-info" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a class="panel-block is-active">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          bulma
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          marksheet
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          minireset.css
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          jgthms.github.io
        </a>
      </article>
    </div>
    <br />
    <div>
      <article class="panel is-info">
        <p class="panel-heading">Info</p>
        <p class="panel-tabs">
          <a class="is-active">All</a>
          <a>Public</a>
          <a>Private</a>
          <a>Sources</a>
          <a>Forks</a>
        </p>
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input is-info" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a class="panel-block is-active">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          bulma
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          marksheet
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          minireset.css
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          jgthms.github.io
        </a>
      </article>
    </div>
    <div>
      <article class="panel is-info">
        <p class="panel-heading">Info</p>
        <p class="panel-tabs">
          <a class="is-active">All</a>
          <a>Public</a>
          <a>Private</a>
          <a>Sources</a>
          <a>Forks</a>
        </p>
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input is-info" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a class="panel-block is-active">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          bulma
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          marksheet
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          minireset.css
        </a>
        <a class="panel-block">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          jgthms.github.io
        </a>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      orders: []
    };
  },
  mounted() {
    this.get_orders();
  },
  methods: {
    get_orders() {
      this.orders = [
        {
          table: "1-A",
          time_elapsed: 2,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        },
        {
          table: "5",
          time_elapsed: 10,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        },
        {
          table: "llevar",
          time_elapsed: 2,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        },
        {
          table: "domicilio",
          time_elapsed: 9,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        }
      ];
    }
  }
};
</script>

<style>
</style>