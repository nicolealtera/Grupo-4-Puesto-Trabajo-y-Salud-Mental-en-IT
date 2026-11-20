create or replace view salud_mental as
-- primero se creo una cte paraagregarle un valor numerico a las variables de la escala de perjuico solo para el anio 2016
with  scale as (
select
h.participanteID,
h.encuestaID,
case 
  when h.afecta_carrera = 'Yes' then 3
  when h.afecta_carrera = 'Maybe' then 2
  when h.afecta_carrera = 'No' then 1
  else null
  end as affects,
case 
  when h.comentarios_malos = 'Yes' then 3
  when h.comentarios_malos = 'Maybe' then 2
  when h.comentarios_malos = 'No' then 1
  else null
  end as bad_coment,
case 
  when h.consecuencias_negativas = 'true' then 2
  when h.consecuencias_negativas = 'false' then 1
  else null
  end as consequences,
case 
  when h.crees_te_verian_mal = 'Yes, they do' then 5
  when h.crees_te_verian_mal = 'Yes, I think they would' then 4
  when h.crees_te_verian_mal = 'Maybe' then 3
  when h.crees_te_verian_mal = 'No, I don''t think they would' then 2
  when h.crees_te_verian_mal = 'No, they do not' then 1
  else null
  end as ven_mal
from HECHOS h
WHERE h.encuestaID = 2016
 )
-- agregar las columnas y cambiar nombres a ingles
select
u.paistexto as country_name,
u.Estadotexto as state_name,
t.puestotexto as role_name,
t.nivel_jerarquico as hierarchical_level,
t.independiente_trabajo as independent_work,
t.trabajo_remoto as remote_work,
p.edad as age,
p.condiciones_diagnosticadas as diagnoses,
p.busco_tratamiento as look_for_treatment,
p.diagnostico_oficial as official_diagnosis,
p.participanteID as userID,
h.encuestaID as surveyID,
h.Encuestatexto as surveytext,
t.puesto_trabajoID as work_roleID,
u.ubicacionID as locationID,
h.afecta_carrera as affects_career,
h.interfiere_trabajo as work_interferences,
h.crees_te_verian_mal as think_they_lookyou_bad,
h.comentarios_malos as bad_comments,
h.consecuencias_negativas as negative_consequences,
h.recursos_empresa_ayuda_mental as company_resources,
h.conoces_opciones_ayuda as know_help_options,
h.beneficios_salud_mental as company_benefits,
h.anonimato_protegido as protected_anonymity,
h.discucion_formal_salud_mental as company_formal_discussions,
case
  when p.generotexto = 'Masculino' then 'Male'
  when p.generotexto = 'Femenino' then 'Female'
  when p.generotexto = 'Otro' then 'Other'
end as gender,
case
  when t.nivel_jerarquico = 'Operativo' then 'Operative'
  when t.nivel_jerarquico = 'Coodinacion' then 'Coordination'
  when t.nivel_jerarquico = 'Directivo' then 'Directive'
  when t.nivel_jerarquico = 'Excluir' then 'Exclude'
  else t.nivel_jerarquico
end as hierarchical_level,
--volver escala una proporcion para que todas valgan lo mismo
round(
  (coalesce(e.affects, 0) / 3.0) + 
  (coalesce(e.bad_coment, 0) / 3.0) + 
  (coalesce (e.consequences, 0) / 2.0) + 
  (coalesce(e.ven_mal, 0) / 5.0),
2) as damage_scale,
-- grupo de edad
case 
  when edad between 18 and 24 then '18-24'
  when edad between 25 and 34 then '25-34'
  when edad between 35 and 44 then '35-44'
  when edad between 45 and 54 then '45-54'
  when edad >= 55 then '55+'
 end as age_group,
from HECHOS h
left join DIM_PARTICIPANTE p on h.participanteID = p.participanteID
left join DIM_TRABAJO t on t.puesto_trabajoID = h.puesto_trabajoID
left join DIM_UBICACION u on u.ubicacionID = h.ubicacionID
left join scale e on h.participanteID = e.participanteID and h.encuestaID = e.encuestaID;