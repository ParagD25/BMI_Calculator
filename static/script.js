'use strict'

const submitBtn = document.querySelector('.submitBtn');
const modal = document.querySelector('.modal_box');
const closeModalBtn = document.querySelector('.close_modal')

submitBtn.addEventListener('click',()=>{
    modal.classList.add('open_modal');
})
closeModalBtn.addEventListener('click',()=>{
    modal.classList.remove('open_modal');
})