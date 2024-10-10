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
Si bien en la ecuación anterior está escrito que dicho potencial depende de la posición de cada una de las dos partículas, la dependencia es más bien con la distancia entre ambas (que, a su vez, depende de las posiciones). Si queremos obtener la fuerza sobre cada partícula a partir del potencial, no tenemos que hacer otra cosa más que calcular su gradiente. Es decir, $$\mathbf{F}_1 = -\nabla_1 U(\mathbf{r}_1, \mathbf{r}_2)$$ y $$mathbf{F}_2 = -\nabla_2 U(\mathbf{r}_1, \mathbf{r}_2)$$, donde los subíndices indican con respecto a las coordenadas de qué partícula hay que derivar.

## Resolución