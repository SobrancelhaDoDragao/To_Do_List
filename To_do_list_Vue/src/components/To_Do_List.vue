<template>

<div id="buttonNew">

<form @submit.prevent="createTask">
  <input class="inputCriarTarefa" type="text" v-model="task.name" >
  <button class="butao">New +</button>
</form>
  
</div>

<div id="to_do">

    <h2>To Do</h2>

        <div id="tarefas">
              <TransitionGroup name="list">


                  <div class="tarefa" v-for="task in tasks" :key="task.id">
                      
                      <div class="grouptarefa">
                          <button class="botaoDone" v-on:click.prevent="TaskDone(task)">Done</button>
                      
                          <span class="TarefaTexto">{{task.name}}</span>
                      </div>
                      
                      <span class="excluir" v-on:click.prevent="DeleteTask(task)" >X</span>
                  </div>

              </TransitionGroup>
        </div>
</div>

<div id="done">

      <h2>Done</h2>

        <TransitionGroup name="list">

            <div class="tarefaDone"  v-for="task in taskDone" :key="task.id">

                <span class="TarefaTexto TarefaTextoDone">{{task.name}}</span>

                <span class="excluir" v-on:click.prevent="DeleteTask(task)" >X</span>
            </div>

        </TransitionGroup>
</div>

</template>

<script>

export default {
    name: 'To_Do_List',

      data(){
          return{
              task:{},
              tasks:[],
              taskDone:[],
          }
      },

      async created(){
          await this.getTask();
      },

      methods: {
  
        async getTask(){
          var reponse = await fetch('/api/To_do_list/');
          
          this.task = await reponse.json();
          
          this.tasks = [];
          this.taskDone = [];
  
          for (let dado in this.task) {
            
            if(this.task[dado].status == 0){
              //Tarefa não concluida
              this.tasks.push(this.task[dado])
            }else{
              //Tarefa concluida
              this.taskDone.push(this.task[dado])
            }
          }
  
          this.task = {}
  
        },
        async createTask(){
  
            this.task.status = 0;
  
            await fetch('/api/To_do_list/', {
              method: 'post',
              headers:{
                'Content-Type':'application/json'
              },
              body: JSON.stringify(this.task)
            });
            
            await this.getTask();
  
            this.task = {};
        },
  
        async TaskDone(task){
  
            task.status = 1;
  
            await fetch(`/api/To_do_list/${task.id}/`, {
              method: 'put',
              headers:{
                'Content-Type':'application/json'
              },
              body: JSON.stringify(task)
            });
            
            this.task = {};
  
            await this.getTask();
  
        },
        async DeleteTask(task){
  
          await fetch(`/api/To_do_list/${task.id}/`, {
              method: 'delete',
              headers:{
                'Content-Type':'application/json'
              },
              body: JSON.stringify(task)
            });
            
            this.task = {};
  
            await this.getTask();
  
        }
  
      }
  }
  </script>