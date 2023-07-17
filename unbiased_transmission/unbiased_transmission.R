# This code is literally copied from https://acerbialberto.com/IBM-cultevo/unbiased-transmission.html
# "Individual-based models of cultural evolution, A step-by-step guide using R" by Alberto Acerbi, Alex Mesoudi, Marco Smolla
# for more background, more models and more code please check it out!


# have a look at the unbiased_transmission_1 function
# TODOs: can you explain what each line does? 

library(tidyverse)

unbiased_transmission_1 <- function(N, t_max) {
    # TODO
    population <- tibble(trait = sample(c("A", "B"), N, replace = TRUE))

    # TODO
    output <- tibble(generation = 1:t_max, p = rep(NA, t_max))

    # TODO
    output$p[1] <- sum(population$trait == "A") / N

    # TODO
    for (t in 2:t_max) {

        # Copy individuals to previous_population tibble
        previous_population <- population 

        # Randomly copy from previous generation
        population <- tibble(trait = sample(previous_population$trait, N, replace = TRUE))

        # Get p and put it into output slot for this generation t
        output$p[t] <- sum(population$trait == "A") / N 
    }
    # Export data from function
    output
}

# this just plots your tibble 
plot_single_run <- function(data_model) {
    ggplot(data = data_model, aes(y = p, x = generation)) +
    geom_line() +
    ylim(c(0, 1)) +
    theme_bw() +
    labs(y = "p (proportion of individuals with trait A)")
}


# TODO: play around with different parameters! any observations?
data_model <- unbiased_transmission_1(N = TODO, t_max = TODO)
plot_single_run(data_model)

# TODO: can you plot multiple runs? (you can also check out the code on 
# https://acerbialberto.com/IBM-cultevo/unbiased-transmission.html and follow that tutorial!)