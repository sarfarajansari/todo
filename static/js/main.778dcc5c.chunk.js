(this.webpackJsonptodo=this.webpackJsonptodo||[]).push([[0],[,,,,,,,,,,,,,,,,function(e,t,n){},function(e,t,n){},,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){"use strict";n.r(t);var a=n(2),c=n.n(a),s=n(7),i=n.n(s),r=(n(16),n(3)),o=(n(17),n(1));function l(){var e=Object(a.useState)(new Date),t=Object(r.a)(e,2),n=t[0],c=t[1];return Object(a.useEffect)((function(){var e=setInterval((function(){return c(new Date)}),1e3);return function(){clearInterval(e)}}),[]),Object(o.jsxs)(o.Fragment,{children:[Object(o.jsx)("div",{className:"box-element clock-container",children:n.toDateString()}),Object(o.jsxs)("p",{className:"time",children:[" ",n.toLocaleTimeString()," "]})]})}n(19);var j=function(e){return Object(o.jsxs)("div",{className:"animation-area",children:[Object(o.jsxs)("ul",{className:"box-area",children:[Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{})]}),e.children]})},d=(n(20),function(){return Object(o.jsxs)("div",{style:{height:"100%"},children:[Object(o.jsx)("div",{className:"nav-container",children:Object(o.jsx)("h1",{children:"TODO APP"})}),Object(o.jsx)("hr",{})]})}),u=(n(21),n(22),n(5)),b=n.n(u),m=n(8),h={url:"https://sarfaraj4444.pythonanywhere.com"};function O(){return(O=Object(m.a)(b.a.mark((function e(t,n){var a,c,s,i=arguments;return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=i.length>2&&void 0!==i[2]?i[2]:"",e.next=3,fetch(h.url+t);case 3:return c=e.sent,e.next=6,c.json();case 6:return s=e.sent,n(s),a&&a(0),"token"in s&&localStorage.setItem("taskToken",s.token),e.abrupt("return",0);case 11:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function x(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"",a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"";t.token=localStorage.getItem("taskToken");var c={"Content-Type":"application/json"};null!==localStorage.getItem("Token")&&(c.Authorization="Token "+localStorage.getItem("Token"));var s={method:"POST",headers:c,body:JSON.stringify(t)};fetch(h.url+e,s).then((function(e){return e.json()})).then((function(e){n&&n(e),a&&a(0)}))}n(24);var f=n(9),g=function(e){var t=e.task;return t.done?Object(o.jsx)(f.a,{color:"rgb(0, 255, 0)"}):Object(o.jsx)("input",{className:"checkbox",type:"checkbox",name:"task"+String(t.id),onClick:function(t){var n="p"+String(e.index),a=localStorage.getItem("taskToken");t.target.checked?(t.target.checked=!1,document.getElementById(n).style.textDecoration="line-through",document.getElementById(n).style.textDecorationColor="rgba(15, 19, 66, 1)",document.getElementById(n).parentNode.style.animation="fade 0.8s linear forwards",x("/todo/complete/",{token:a,id:e.task.id}),setTimeout(e.update(0,a),50),setTimeout((function(){document.getElementById(n).style.textDecoration="none",document.getElementById(n).parentNode.style.animation="none",document.getElementById(n).parentNode.style.opacity=1}),700)):document.getElementById(n).style.textDecoration="none"}})},p=function(e){return Object(o.jsx)("div",{className:"list-container",children:e.list.map((function(t,n){var a=300*n+300-30*n;a>7e3&&(a=7e3);var c=String(a)+"ms";return Object(o.jsxs)("div",{className:"list-item",style:{animationDuration:c},children:[Object(o.jsxs)("div",{style:{background:"none"},children:[Object(o.jsx)(g,{setdata:e.setdata,update:e.update,task:t,index:n})," "]}),Object(o.jsx)("p",{className:"p",id:"p"+String(n),children:t.task})]})}))})},v=(n(25),function(e){var t=Object(a.useState)(""),n=Object(r.a)(t,2),c=n[0],s=n[1];return Object(o.jsxs)("form",{onSubmit:function(t){t.preventDefault(),x("/todo/post/",{task:c}),setTimeout((function(){1===e.type?(document.getElementById("todo").selected="selected",e.refresh()):e.update(0,localStorage.getItem("taskToken")),s("")}),30)},className:"form-container",children:[Object(o.jsx)("input",{type:"text",required:!0,value:c,onChange:function(e){s(e.target.value)},name:"task",placeholder:"New Task"}),Object(o.jsx)("input",{type:"submit",value:"Add Task"})]})}),k=function(){var e=Object(a.useState)(0),t=Object(r.a)(e,2),n=t[0],c=t[1],s=Object(a.useState)({tasks:[]}),i=Object(r.a)(s,2),l=i[0],j=i[1];Object(a.useEffect)((function(){var e="create";null!==localStorage.getItem("taskToken")&&(e=localStorage.getItem("taskToken")),d(n,e)}),[n]);var d=function(e,t){!function(e,t){O.apply(this,arguments)}("/todo/get/"+String(e)+"/"+t+"/",j)};return Object(o.jsxs)("div",{className:"any-container content-container",children:[Object(o.jsx)(v,{refresh:function(){j({tasks:[]}),c(0)},type:n,update:d}),Object(o.jsx)("div",{id:"lisType",children:Object(o.jsxs)("select",{onChange:function(e){j({tasks:[]}),c(e.target.value)},children:[Object(o.jsx)("option",{id:"todo",value:0,children:"TODO"}),Object(o.jsx)("option",{value:1,children:"Complete Task"})]})}),Object(o.jsx)(p,{list:l.tasks,setdata:j,update:d})]})},y=n(6),S=n(10),N=n(11);n(26);function T(){return Object(o.jsxs)("div",{className:"footer-container",children:[Object(o.jsxs)("div",{className:"tag",children:["@2021 Sarfarajansari ",Object(o.jsx)("hr",{})]}),Object(o.jsx)("p",{style:{textAlign:"center",fontSize:"2rem",marginBottom:"1rem",color:"white"},children:"Social"}),Object(o.jsxs)("div",{className:"social-item",children:[Object(o.jsxs)("a",{href:"https://twitter.com/Sarfraj49393426",children:[Object(o.jsx)(y.b,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Twitter"})]}),Object(o.jsxs)("a",{href:"https://www.instagram.com/sarfarajansari_/",children:[Object(o.jsx)(S.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Instagram"})]}),Object(o.jsxs)("a",{href:"https://github.com/sarfarajansari",children:[Object(o.jsx)(y.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Github"})]}),Object(o.jsxs)("a",{href:"https://www.linkedin.com/in/sarfaraj-ansari-a0a9441b9/",children:[Object(o.jsx)(N.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"LinkedIn"})]})]})]})}var I=function(){return Object(o.jsx)(o.Fragment,{children:Object(o.jsx)(j,{children:Object(o.jsxs)("div",{id:"grid",children:[Object(o.jsxs)("div",{id:"navbar",children:[Object(o.jsx)(d,{})," "]}),Object(o.jsxs)("div",{id:"content",children:[Object(o.jsx)(l,{}),Object(o.jsx)(k,{})]}),Object(o.jsxs)("div",{id:"footer",children:[Object(o.jsx)("hr",{}),Object(o.jsx)(T,{}),"  "]})]})})})},w=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,28)).then((function(t){var n=t.getCLS,a=t.getFID,c=t.getFCP,s=t.getLCP,i=t.getTTFB;n(e),a(e),c(e),s(e),i(e)}))};i.a.render(Object(o.jsx)(c.a.StrictMode,{children:Object(o.jsx)(I,{})}),document.getElementById("root")),w()}],[[27,1,2]]]);
//# sourceMappingURL=main.778dcc5c.chunk.js.map