document.addEventListener('DOMContentLoaded',()=>{
  const knowledge={
    'google ads':'Trabajo con estructura de campañas, intención de búsqueda, CTR, CPC, CPA, conversiones y optimización de presupuesto. También conecto campañas con landing pages, GA4 y GTM.',
    'meta ads':'Tengo experiencia con campañas de captación, creatividades, segmentación, remarketing y análisis de CPL, CTR, frecuencia y calidad del lead.',
    'veltriona':'Veltriona es un CRM SaaS para negocios de servicios. Integra clientes, leads, pipeline, agenda, ingresos, automatización y agentes de IA. Mi participación incluye estrategia de producto, experiencia y coordinación técnica.',
    'sia':'SIA’AN KA’AN es un ecosistema digital para wellness y capacitación. Conecta marketing, academia digital, contenidos interactivos, pagos y experiencia del alumno.',
    'herramientas':'Mis herramientas principales incluyen Meta Ads, Google Ads, GA4, GTM, Looker Studio, HubSpot, Zoho, Make, Next.js, Supabase, Prisma, Vercel y Excel.',
    'experiencia':'Mi perfil combina marketing digital, automatización, CRM, analítica y desarrollo de productos digitales. He trabajado especialmente con negocios de servicios, wellness, educación y turismo.',
    'contacto':'Puedes contactarme desde la página Contact o escribirme a tonathiupalma@gmail.com. Estoy disponible para oportunidades profesionales y proyectos remotos.',
    'ingles':'Mi idioma nativo es español y actualmente estoy desarrollando mi inglés profesional de forma progresiva.',
    'automatizacion':'Diseño flujos para reducir tareas manuales, mejorar seguimiento de leads y conectar marketing, CRM, agenda, formularios y reportes.'
  };
  const messages=document.querySelector('#assistantMessages');
  const input=document.querySelector('#assistantInput');
  const form=document.querySelector('#assistantForm');
  const add=(text,type)=>{if(!messages)return;const el=document.createElement('div');el.className=`message ${type}`;el.textContent=text;messages.appendChild(el);messages.scrollTop=messages.scrollHeight;};
  const reply=q=>{const s=q.toLowerCase();const key=Object.keys(knowledge).find(k=>s.includes(k));return key?knowledge[key]:'Puedo contarte sobre mi experiencia, Google Ads, Meta Ads, automatización, herramientas, Veltriona, SIA’AN KA’AN, inglés o contacto.'};
  const ask=q=>{if(!q.trim())return;add(q,'user');setTimeout(()=>add(reply(q),'bot'),220);};
  form?.addEventListener('submit',e=>{e.preventDefault();ask(input.value);input.value='';});
  document.querySelectorAll('.prompt-chip').forEach(b=>b.addEventListener('click',()=>ask(b.dataset.question||b.textContent)));

  const details={
    marketing:['Marketing y performance','Meta Ads, Google Ads, estrategia de campañas, optimización y lectura de KPIs.'],
    automation:['Automatización y CRM','HubSpot, Zoho, Make, seguimiento de leads, procesos comerciales y reducción de tareas manuales.'],
    development:['Producto y desarrollo','Next.js, Supabase, Prisma, Vercel, arquitectura de producto y experiencias digitales.'],
    analytics:['Analítica','GA4, GTM, Looker Studio, Excel, dashboards e interpretación de datos para decisiones.'],
    ai:['IA aplicada','Agentes, asistentes, automatización inteligente y prototipos para atención y productividad.']
  };
  document.querySelectorAll('.skill-panel').forEach(p=>p.addEventListener('click',()=>{
    document.querySelectorAll('.skill-panel').forEach(x=>x.classList.remove('active'));p.classList.add('active');
    const d=details[p.dataset.skill];const box=document.querySelector('#skillDetail');if(d&&box){box.innerHTML=`<h3>${d[0]}</h3><p>${d[1]}</p>`;}
  }));

  const updated=document.querySelector('#lastUpdated');if(updated){updated.textContent=new Intl.DateTimeFormat('es-MX',{dateStyle:'long'}).format(new Date(document.lastModified));}
});