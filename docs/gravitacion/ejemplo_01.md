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

## Spacing

These spacers are available to use for margins and padding with responsive utility classes. Combine these prefixes with a screen size and spacing scale to use them responsively.

| Classname prefix | Related CSS Property          |
|:-----------------|:------------------------------|
| `.m-`            | `margin`                      |
| `.mx-`           | `margin-left`, `margin-right` |
| `.my-`           | `margin top`, `margin bottom` |
| `.mt-`           | `margin-top`                  |
| `.mr-`           | `margin-right`                |
| `.mb-`           | `margin-bottom`               |
| `.ml-`           | `margin-left`                 |

| Classname prefix | Related CSS Property            |
|:-----------------|:--------------------------------|
| `.p-`            | `padding`                       |
| `.px-`           | `padding-left`, `padding-right` |
| `.py-`           | `padding top`, `padding bottom` |
| `.pt-`           | `padding-top`                   |
| `.pr-`           | `padding-right`                 |
| `.pb-`           | `padding-bottom`                |
| `.pl-`           | `padding-left`                  |

Spacing values are based on a `1rem = 16px` spacing scale, broken down into these units:

| Spacer/suffix  | Size in rems  | Rem converted to px |
|:---------------|:--------------|:--------------------|
| `1`            | 0.25rem       | 4px                 |
| `2`            | 0.5rem        | 8px                 |
| `3`            | 0.75rem       | 12px                |
| `4`            | 1rem          | 16px                |
| `5`            | 1.5rem        | 24px                |
| `6`            | 2rem          | 32px                |
| `7`            | 2.5rem        | 40px                |
| `8`            | 3rem          | 48px                |
| `auto`         | auto          | auto                |

Use `mx-auto` to horizontally center elements.

### Applying Spacing Utilities with `{: }`
{: .no_toc .text-delta }

In Markdown, use the `{: }` wrapper to apply custom classes:

```markdown
This paragraph will have a margin bottom of 1rem/16px on large screens.
{: .mb-lg-4 }

This paragraph will have 2rem/32px of padding on the right and left at all screen sizes.
{: .px-6 }
```

## Horizontal Alignment

| CSS Class               | Applied CSS Declaration          |
|:------------------------|:---------------------------------|
| `.float-left`           | `float: left`                    |
| `.float-right`          | `float: right`                   |
| `.flex-justify-start`   | `justify-content: flex-start`    |
| `.flex-justify-end`     | `justify-content: flex-end`      |
| `.flex-justify-between` | `justify-content: space-between` |
| `.flex-justify-around`  | `justify-content: space-around`  |

_Note: any of the `flex-` classes must be used on a parent element that has `d-flex` applied to it._

## Vertical Alignment

| CSS Class              | Applied CSS Declaration         |
|:-----------------------|:--------------------------------|
| `.v-align-baseline`    | `vertical-align: baseline`      |
| `.v-align-bottom`      | `vertical-align: bottom`        |
| `.v-align-middle`      | `vertical-align: middle`        |
| `.v-align-text-bottom` | `vertical-align: text-bottom`   |
| `.v-align-text-top`    | `vertical-align: text-top`      |
| `.v-align-top`         | `vertical-align: top`           |

## Display

Display classes aid in adapting the layout of the elements on a page:

| CSS Class         | Applied CSS Declaration |
|:------------------|:------------------------|
| `.d-block`        | `display: block`        |
| `.d-flex`         | `display: flex`         |
| `.d-inline`       | `display: inline`       |
| `.d-inline-block` | `display: inline-block` |
| `.d-none`         | `display: none`         |

Use these classes in conjunction with the responsive modifiers.

### Applying Display Utilities with `{: }`
{: .no_toc .text-delta }

In Markdown, use the `{: }` wrapper to apply custom classes:

```markdown
This button will be hidden until medium screen sizes:

[ A button ](#url)
{: .d-none .d-md-inline-block }

These headings will be `inline-block`:

### heading 3
{: .d-inline-block }

### heading 3
{: .d-inline-block }
```