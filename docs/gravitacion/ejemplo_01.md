---
title: Ejemplo
layout: default
parent: Gravitación
nav_order: 4
---

# Dos partículas bajo la interacción de la gravedad
{: .no_toc }

Considere dos partículas de masa $$m$$ que interactúan gravitatoriamente entre sí. Las partículas pueden moverse sobre una mesa horizontal libre de rozamiento. En el instante inicial ($$t = 0$$) las partículas se hallan separadas una distancia $$d$$ y se le da a cada una de ellas una velocidad $$\mathbf{v}_0$$ de módulo $$v_0$$ y dirección indicada en la figura.

1. Indique en un diagrama todas las fuerzas que actúan sobre cada partícula. Para el sistema formado por las dos partículas diga, justificando su respuesta, si se conservan o no el impulso lineal, el impulso angular y la energía mecánica total.

2. Halle la velocidad del centro de masa del sistema en el instante inicial. Diga qué tipo de movimiento describe el centro de masa para $$t > 0$$.

3. Para cada una de las partículas, calcule el vector velocidad (componentes paralela y perpendicular al segmento que las une) cuando las partículas se hallan separadas una distancia $$d/2$$.

<img src="../../assets/images/placeholder.png" style="display: block; margin: 0 auto"/>

---

## Repaso

Dos partículas de masas $$m_1$$ y $$m_2$$ y posiciones $$\mathbf{r}_1$$ y $$\mathbf{r}_2$$, respectivamente, que interactúan gravitatoriamente están sujetas a una fuerza que es inversamente proporcional al cuadrado de la distancia que las separa y que actúa a lo largo de la línea que las une, como vemos en la figura siguiente.

<img src="../../assets/images/placeholder.png" style="display: block; margin: 0 auto"/>

La partícula $$m_1$$ está sujeta a la fuerza $$\mathbf{F}_1$$ y la partícula $$m_2$$ está sujeta a la fuerza $$\mathbf{F}_2$$, y sabemos que dichas fuerzas tienen el mismo módulo y sentido contrario: $$\mathbf{F}_2 = -\mathbf{F}_1$$.
$$\mathbf{F}_1$$ es la fuerza que actúa sobre 1 debido a 2 y $$\mathbf{F}_2$$ es la fuerza que actúa en 2 debido a 1.

La forma vectorial de estas fuerzas gravitatorias es

$$\mathbf{F_1} = - G m_1 m_2 \frac{\mathbf{r}_1 - \mathbf{r}_2}{ \left| \mathbf{r}_1 - \mathbf{r}_2 \right|^3 } = - G m_1 m_2 \frac{\mathbf{r}_{12}}{ \left| \mathbf{r}_{12} \right|^3 },$$

y

$$\mathbf{F_2} = - G m_1 m_2 \frac{\mathbf{r}_2 - \mathbf{r}_1}{ \left| \mathbf{r}_2 - \mathbf{r}_1 \right|^3 } = - G m_1 m_2 \frac{\mathbf{r}_{21}}{ \left| \mathbf{r}_{21} \right|^3 }.$$

Sabemos, además, que la fuerza gravitatoria es conservativa y, por ende, tiene asociado un potencial. Dicho potencial tiene la forma

$$U (\mathbf{r}_1, \mathbf{r}_2) = - G \frac{m_1 m_2}{\left| \mathbf{r}_1 - \mathbf{r}_2 \right|}.$$

Si bien en la ecuación anterior está escrito que dicho potencial depende de la posición de cada una de las dos partículas, la dependencia es más bien con la distancia entre ambas (que, a su vez, depende de las posiciones). Si queremos obtener la fuerza sobre cada partícula a partir del potencial, no tenemos que hacer otra cosa más que calcular su gradiente. Es decir, $$\mathbf{F}_1 = -\nabla_1 U(\mathbf{r}_1, \mathbf{r}_2)$$ y $$\mathbf{F}_2 = -\nabla_2 U(\mathbf{r}_1, \mathbf{r}_2)$$, donde los subíndices indican con respecto a las coordenadas de qué partícula hay que derivar.

## Resolución

### Fuerzas

El primer paso para resolver el ejercicio es darnos una idea cuáles son las fuerzas que actúan sobre las partículas involucradas.
Vamos a elegir como sistema de partículas al conjunto de las dos masas (aunque el enunciado lo pide explícitamente, esta es la elección lógica para tener un sistema aislado).
Las únicas fuerzas que actúan en el sistema son las gravitatorias y son internas (porque son ejercidas por cuerpos que pertenecen a nuestro sistema: $$\mathbf{F}_1$$, por ejemplo, es la fuerza que 2 ejerce sobre 1 y como 2 es parte del sistema, entonces $$\mathbf{F}_1$$ es interna).

### Sistema de referencia

En segundo lugar, tenemos que definir el sistema de referencia que vamos a utilizar. En esta clase de problemas suele ser una buena idea pararnos en el centro de masa (CM) y describir todo el movimiento desde allí. Sin embargo, primero tenemos que asegurarnos de que el CM es un sistema válido\footnote{Por ``válido'' quiero decir que sea un sistema inercial; es decir, que tenga aceleración nula. No queremos pelear con fuerzas inerciales acá.} para trabajar. Ya sabemos (desde la guía de momento lineal) que la aceleración del CM está relacionada con la sumatoria de fuerzas externas, es decir

$$M \mathbf{A}_\mathrm{CM} = \sum_i \mathbf{F}_i^\mathrm{ext},$$

donde $$M = m_1 + m_2$$ es la masa total del sistema de partículas, $$\mathbf{A}_\mathrm{CM}$$ es la aceleración del CM y $$\sum_i \mathbf{F}_i^\mathrm{ext}$$ es la suma de todas las fuerzas externas que actúan sobre el sistema. En este problema no tenemos fuerzas externas (las gravitatorias son internas) y, por lo tanto, ocurre que

$$\mathbf{A}_\mathrm{CM} (t) = 0$$

y, por lo tanto, lo podemos utilizar como sistema de referencia.

Si vamos a trabajar desde el CM vamos a tener que saber dónde se encuentra (al menos inicialmente) y cuál es su velocidad (que va a ser constante, porque su aceleración es nula). La velocidad del centro de masa está dada por

$$\mathbf{V}_\mathrm{CM} = \frac{m \mathbf{v}_1 + m \mathbf{v}_2}{2 m}.$$

Como las partículas tienen la misma masa y velocidades contrarias en el instante inicial, $$\mathbf{V}_\mathrm{CM} (t=0) = 0$$. Por otro lado, como el CM no está acelerado, sabemos entonces que la velocidad va a ser nula no sólo en el instante inicial pero para todo tiempo:

$$\mathbf{V}_\mathrm{CM} (t) = 0.$$

Entonces, el CM no sólo tiene aceleración nula pero también velocidad nula para todo tiempo (está fijo durante toda la evolución del sistema).

Veamos ahora dónde está utilizando la información de las partículas en el instante inicial. La posición del CM está dada por

$$\mathbf{R}_\mathrm{CM} = \frac{m \mathbf{r}_1 + m \mathbf{r}_2}{2 m}.$$

Pueden elegir algún sistema inercial cualquiera para hacer la cuenta anterior y luego pasar al CM. Sin embargo, esto no es necesario porque las dos partículas tienen la misma masa; por ende, el CM va a estar en el punto medio de la recta que las une a $$t=0$$ y se quedará allí independientemente del movimiento de las partículas. Una vez que tengamos un sistema de referencia fijo al CM, ocurrirá, por supuesto, que

$$\mathbf{R}_\mathrm{CM} (t) = 0.$$

La figura siguiente muestra la configuración inicial del sistema, la posición del CM y un sistema de coordenadas cartesiano ubicado allí.

<img src="../../assets/images/placeholder.png" style="display: block; margin: 0 auto"/>

Noten que con este análisis ya respondimos una parte del inciso (a) y todo el inciso (b).
























