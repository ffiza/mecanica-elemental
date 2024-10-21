---
title: Ejemplo
layout: default
parent: Gravitación
nav_order: 4
---

# Dos partículas bajo la interacción de la gravedad
{: .no_toc }

Resolución de un ejercicio sencillo en el cual dos partículas interactúan mediante una fuerza gravitatoria.
{: .fs-6 .fw-300 }

---

## Enunciado

Considere dos partículas de masa $$m$$ que interactúan gravitatoriamente entre sí. Las partículas pueden moverse sobre una mesa horizontal libre de rozamiento. En el instante inicial ($$t = 0$$) las partículas se hallan separadas una distancia $$d$$ y se le da a cada una de ellas una velocidad $$\mathbf{v}_0$$ de módulo $$v_0$$ y dirección indicada en la figura.

1. Indique en un diagrama todas las fuerzas que actúan sobre cada partícula. Para el sistema formado por las dos partículas diga, justificando su respuesta, si se conservan o no el impulso lineal, el impulso angular y la energía mecánica total.

2. Halle la velocidad del centro de masa del sistema en el instante inicial. Diga qué tipo de movimiento describe el centro de masa para $$t > 0$$.

3. Para cada una de las partículas, calcule el vector velocidad (componentes paralela y perpendicular al segmento que las une) cuando las partículas se hallan separadas una distancia $$d/2$$.

<img src="../../assets/images/fig_01.png" style="display: block; margin: 0 auto"/>

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

En segundo lugar, tenemos que definir el sistema de referencia que vamos a utilizar. En esta clase de problemas suele ser una buena idea pararnos en el centro de masa (CM) y describir todo el movimiento desde allí. Sin embargo, primero tenemos que asegurarnos de que el CM es un sistema válido[^1] para trabajar. Ya sabemos (desde la guía de momento lineal) que la aceleración del CM está relacionada con la sumatoria de fuerzas externas, es decir

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

### Teoremas de conservación

Veamos ahora qué ocurre con los teoremas de conservación. Queremos saber si se conservan (o no) el momento lineal $$\mathbf{p}$$, el momento angular $$\mathbf{L}^\mathrm{CM}$$ (que vamos a medir desde el origen de coordenadas, aunque ---en este caso en particular--- se conserva desde cualquier punto) y la energía mecánica $$E$$.

#### Momento lineal

La conservación del momento lineal del sistema está dado por la suma de todas las fuerzas externas, es decir:

$$\frac{\mathrm{d} \mathbf{p}}{\mathrm{d} t} = \sum_i \mathbf{F}_i^\mathrm{ext}.$$

Ya analizamos esto cuando hablamos del CM, y dijimos que no hay fuerzas externas. Por ende, el momento lineal del sistema se conserva.

#### Momento angular

El momento angular desde el CM se conserva si la suma de los torques externos desde el CM se anula, es decir:

$$\frac{\mathrm{d} \mathbf{L}^\mathrm{CM}}{\mathrm{d} t} = \sum_i \boldsymbol{\tau}_i^\mathrm{CM}.$$

(En la ecuación anterior no puse el superíndice que indica que los torques son *externos* para no sobrecargar la notación, pero no se olviden de eso). Como antes, al no haber fuerzas externas al sistema, tampoco hay torques externos. Por lo tanto, el momento angular medido desde el origen de coordenadas (el CM) se conserva.

#### Energía mecánica

La conservación de la energía mecánica esta determinada por el trabajo de las fuerzas no conservativas, es decir:

$$\Delta E = W_\mathrm{FNC}.$$

Acá hay que tener un poco más de cuidado porque en la ecuación anterior hay que considerar *todas* las fuerzas, tanto las externas como las internas. Ya dijimos que en este problema no hay fuerzas externas, pero sí hay internas: las dos gravitatorias. Sin embargo, como ya saben, las fuerzas gravitatorias son conservativas (derivan de un potencial) y, por lo tanto, no juegan ningún rol en la conservación de $$E$$. La energía mecánica, entonces, también se conserva.

En resumen: tanto $$\mathbf{p}$$, $$\mathbf{L}^\mathrm{CM}$$ y $$E$$ son cantidades conservadas del problema. Esto responde lo que quedaba del inciso (a).

### Velocidades de las partículas

En el inciso (c) se nos pide determinar la velocidad para cada una de las partículas cuando las mismas están separadas una distancia $$d/2$$. Vamos a resolverlo en general, para una distancia cualquiera, y luego lo especificamos para el caso $$d/2$$.

Como se ve en la figura XXXXXXXXXX, vamos a llamar 1 a la partícula que inicialmente se encuentra a la derecha del CM y 2 a la otra[^2].

Notemos primero que como el CM está quieto en el origen de coordenadas, las posiciones de 1 y 2 no son independientes. De hecho,

$$\mathbf{R}_\mathrm{CM} = \frac{m \mathbf{r}_1 + m \mathbf{r}_2}{2 m} = 0,$$

por lo que

$$\mathbf{r}_2 = - \mathbf{r}_1.$$

Lo mismo vale, además, para las velocidades:

$$\mathbf{V}_\mathrm{CM} = \frac{m \mathbf{v}_1 + m \mathbf{v}_2}{2 m} = 0.$$

Entonces,

$$\mathbf{v}_2 = - \mathbf{v}_1.$$

La idea para resolver esta parte es, por supuesto, utilizar los teoremas de conservación. Sabemos que tanto $$\mathbf{p}$$, $$\mathbf{L}^\mathrm{CM}$$ y $$E$$ son cantidades conservadas del problema, es decir, su valor se mantiene constante a lo largo de toda la evolución. Calculemos entonces los valores iniciales del momento angular y la energía mecánica[^3], los que corresponden a la configuración de la figura XXXXX.

El momento angular inicial $$\mathbf{L}_0^\mathrm{CM}$$ está dado por

$$\begin{align*} \mathbf{L}_0^\mathrm{CM} &= \mathbf{L}^\mathrm{CM} (t=0), \\ &= m_1 \mathbf{r}_1 (t=0) \times \mathbf{v}_1 (t=0) + m_2 \mathbf{r}_2 (t=0) \times \mathbf{v}_2 (t=0), \\ &= m \mathbf{r}_1 (t=0) \times \mathbf{v}_1 (t=0) + m \mathbf{r}_2 (t=0) \times \mathbf{v}_2 (t=0), \\ &= 2 m \mathbf{r}_1 (t=0) \times \mathbf{v}_1 (t=0), \\ &= 2m \left( \frac{d}{2} \hat{x} \right) \times \left( -v_0 \cos \alpha \hat{x} - v_0 \sin \alpha \hat{y} \right), \\ &= - m d v_0 \sin \alpha \hat{z}. \end{align*}$$

En la cuenta anterior, tenemos que usar que $$\mathbf{r}_2 = - \mathbf{r}_1$$ y que $$\mathbf{v}_2 = - \mathbf{v}_1$$. Les queda a ustedes descomponer los vectores.

La energía mecánica inicial $$E_0$$ es

$$\begin{align*} E_0 &= E (t=0), \\ &= K_1 (t=0) + K_2 (t=0) + U (t=0), \\ &= \frac{1}{2} m v_0^2 + \frac{1}{2} m v_0^2 - G \frac{m^2}{d}, \\ &= m v_0^2 - G \frac{m^2}{d}. \end{align*}$$

En la cuenta anterior usamos que $$\mathbf{r}_2 = - \mathbf{v}_1$$, que inicialmente la velocidad de 1 es $$v_0$$ y que la distancia inicial entre las partículas es $$\lvert \mathbf{r}_1 - \mathbf{r}_2 \rvert = d$$.

Ahora tenemos que escribir el momento angular y la energía mecánica en un instante cualquiera para así poder igual a los valores iniciales y despejar lo que nos interesa. Para eso, sin embargo, es conveniente usar coordenadas polares. Esto es así porque las fuerzas gravitatorias van a hacer que las partículas giren alrededor del CM, y ya sabemos que los problemas donde las cosas giran suelen ser más sencillos en polares.
La Fig.~\ref{fig:config_gen} muestra el sistema de partículas en una configuración genérica y el sistema de coordenadas polares que vamos a usar para describir el movimiento (que apunta hacia la partícula 1). En gris, para tener la referencia, se muestra la configuración del instante inicial.

<img src="../../assets/images/placeholder.png" style="display: block; margin: 0 auto"/>

En este sistema de coordenadas tenemos que $$\mathbf{r}_1 = r_1 \hat{r}$$ y $$\mathbf{v}_1 = \dot{r}_1 \hat{r} + r_1 \dot{\theta}_1 \hat{\theta}$$. Para la partícula 2, ya sabemos que, en cualquier instante, $$\mathbf{r}_2 = -\mathbf{r}_1$$ y $$\mathbf{v}_2 = -\mathbf{v}_1$$.

El momento angular desde CM en un instante cualquiera $$\mathbf{L}^\mathrm{CM}$$ es, entonces,

$$\begin{align*} \mathbf{L}^\mathrm{CM} &= m_1 \mathbf{r}_1 \times \mathbf{v}_1 + m_2 \mathbf{r}_2 \times \mathbf{v}_2, \\ &= 2 m \mathbf{r}_1 \times \mathbf{v}_1, \\ &= 2m r_1 \hat{r} \times \left( \dot{r}_1 \hat{r} + r_1 \dot{\theta}_1 \hat{\theta} \right), \\ &= 2 m r_1^2 \dot{\theta}_1 \hat{z}. \end{align*}$$

La energía mecánica en un instante cualquiera $$E$$ es

$$\begin{align*} E &= K_1 + K_2 + U, \\ &= \frac{1}{2} m v_1^2 + \frac{1}{2} m v_2^2 - G \frac{m^2}{\left| \mathbf{r}_1 - \mathbf{r}_2 \right|}, \\ &= m v_1^2 - G \frac{m^2}{\left| 2 \mathbf{r}_1 \right|}, \\ &= m \left( \dot{r}_1^2 + r_1^2 \dot{\theta}_1^2 \right) - G \frac{m^2}{2 r_1}. \end{align*}$$

Lo que tenemos que hacer a continuación es plantear la ecuaciones $$\mathbf{L}^\mathrm{CM} = \mathbf{L}_0^\mathrm{CM}$$ y $$E = E_0$$. Tenemos, por lo tanto:

$$\begin{cases}
        \mathbf{L}^\mathrm{CM} = \mathbf{L}_0^\mathrm{CM} \implies 2 m r_1^2 \dot{\theta}_1 \hat{z} = - m d v_0 \sin \alpha \hat{z} , \\
        E = E_0 \implies m \left( \dot{r}_1^2 + r_1^2 \dot{\theta}_1^2 \right) - G \frac{m^2}{2 r_1} = m v_0^2 - G \frac{m^2}{d}.
\end{cases}$$

Como el objetivo es encontrar la velocidad de las partículas, tenemos que despejar $$\dot{r}_1$$ y $$\dot{\theta}_1$$ de las ecuaciones anteriores en función de la coordenada $$r_1$$ (todo lo demás es dato). Despejar la velocidad angular es inmediato porque sale directamente de la ecuación para el momento angular:

$$\dot{\theta}_1 ( r_1 ) = - \frac{d v_0 \sin \alpha}{2 r_1^2}.$$

El despeje de la velocidad radial es un poquito más complicado así que les queda a ustedes verificar que el resultado es

$$\dot{r}_1^2 ( r_1 ) = v_0^2 - \frac{d^2 v_0^2 \sin^2 \alpha}{4 r_1^2} + G m \left( \frac{1}{2 r_1} - \frac{1}{d} \right).$$

El enunciado pedía las velocidades de las partículas cuando la separación entre ambas es $$d/2$$. ¿Qué valor tenemos que darle a $$r_1$$ para que eso se cumpla? Recuerden que $$r_1$$ es la distancia entre el CM y la partícula 1, que es, a su vez, la mitad de la distancia que hay entre las partículas. Por lo tanto, para que 1 y 2 estén separadas $$d/2$$ tenemos que usar $$r_1 = d/4$$. Reemplazando ese valor, nos quedan las velocidades

$$\dot{\theta}_1 = - \frac{8 v_0 \sin \alpha}{d}$$

y

$$\dot{r}_1^2 = v_0^2 \left( 1 - 4 \sin^2 \alpha \right) + \frac{Gm}{d}.$$

Les dejo una pregunta sobre estos resultados. Noten que $$\dot{r}_1$$ está definido por una raíz cuadrada. ¿Cuál es la interpretación física de que el argumento de dicha raíz sea negativo?

### Simulaciones

Para terminar, les dejo los resultados de unas simulaciones de este ejercicio para distintos casos. Todos los enlaces llevan a YouTube. En cada video se muestran las trayectorias de las dos partículas, el tiempo y la energía total del sistema (abajo a la izquierda) y barras que indican los niveles de energía mecánica $$E$$, potencial $$U$$ y cinética $$K$$ (si las barras están hacia arriba la energía es positiva y viceversa).

1. [Ejemplo 1]. En este caso, la energía del sistema es nula y, por lo tanto, las partículas describen órbitas parabólicas.
2. [Ejemplo 2]. En este caso, la energía del sistema también es nula, pero las condiciones iniciales del sistema están elegidas para que el punto de máximo acercamiento[^4] sea exactamente cuando la distancia entre las partículas es $d/2$.
3. [Ejemplo 3]. En este caso, la energía del sistema es negativa. Esto quiere decir que las órbitas son cerradas (elípticas o, si la energía es igual al valor mínimo del potencial efectivo, circulares; sin embargo, se ve a ojo que las órbitas son elípticas).
4. [Ejemplo 4]. Este caso también muestra órbitas elípticas, pero más excéntricas que el caso anterior. Noten, sin embargo, que las órbitas están rotando (y además, que la energía no parece conservarse, lo cual sabemos que no puede ocurrir). Esto no es una solución válida del problema de dos cuerpos que vimos en clase. Entonces, ¿qué está pasando? Lo que ocurre está relacionado con $$\Delta t$$ (el espaciado entre puntos sucesivos del vector de tiempos que se usa para resolver el problema numéricamente). El hecho de que las órbitas roten es consecuencia de errores numéricos que surgen por no usar un $$\Delta t$$ lo suficientemente chico.
5. [Ejemplo 5]. Este caso es el mismo que el anterior, sólo que la integración se realizó con un paso temporal ($$\Delta t$$) más chico. Como resultado, obtengo las mismas órbitas, solamente que ahora no están en rotación.

----

[^1]: Por *válido* quiero decir que sea un sistema inercial; es decir, que tenga aceleración nula. No queremos pelear con fuerzas inerciales acá.
[^2]: Por supuesto, es irrelevante qué número le ponemos a cada una.
[^3]: El momento lineal es nulo, ya lo vimos antes cuando analizamos el CM porque $$\mathbf{p} = 2m \mathbf{V}_\mathrm{CM}$$.
[^4]: ¿Cuál es la condición que deben cumplir las velocidades de las partículas en el punto de máximo acercamiento?

[Ejemplo 1]: https://youtu.be/I3U7MGbQIdA?si=nbO7dpa_yBoRGjr_
[Ejemplo 2]: https://youtu.be/8C-GpehjkiU?si=Hkg5Vi_8kBwA6iA-
[Ejemplo 3]: https://youtu.be/itIvMWKCWQ0?si=NVcSr3LB6dh4iz_d
[Ejemplo 4]: https://youtu.be/DUorm2F3x1w?si=2NiOisa_1C9Evg1s
[Ejemplo 5]: https://youtu.be/Qin4mXVgOFM?si=1DqUeAp5D25hg4lG
