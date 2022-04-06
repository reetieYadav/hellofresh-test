-- CREATE USER demodb;
-- CREATE DATABASE demodb;
-- GRANT ALL PRIVILEGES ON DATABASE demodb TO demodb;

-- DROP TABLE [IF EXISTS]
--    ingredients,
--    weekly_menu,
--    recipes,
--    menu_recipe,
--    recipe_ingredient
-- [CASCADE | RESTRICT];
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS weekly_menu;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS menu_recipe;
DROP TABLE IF EXISTS recipe_ingredient;


-- public.ingredients sql table

CREATE SEQUENCE ingredients_ingredient_id_seq;
CREATE TABLE IF NOT EXISTS public.ingredients
(
    ingredient_id integer NOT NULL DEFAULT nextval('ingredients_ingredient_id_seq'),
    ingredient_name character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ingredients_pkey PRIMARY KEY (ingredient_id)
);

alter table ingredients
    owner to demodb;

ALTER SEQUENCE ingredients_ingredient_id_seq
OWNED BY public.ingredients.ingredient_id;


-- public.weekly_menu sql table

CREATE SEQUENCE weekly_menu_menu_id_seq;

CREATE TABLE IF NOT EXISTS public.weekly_menu
(
    menu_id integer NOT NULL DEFAULT nextval('weekly_menu_menu_id_seq'),
    menu_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT weekly_menu_pkey PRIMARY KEY (menu_id)
);

alter table weekly_menu
    owner to demodb;

ALTER SEQUENCE weekly_menu_menu_id_seq
OWNED BY public.weekly_menu.menu_id;



-- public.recipes sql table
CREATE SEQUENCE recipes_recipe_id_seq;

CREATE TABLE IF NOT EXISTS public.recipes
(
    recipe_id integer NOT NULL DEFAULT nextval('recipes_recipe_id_seq'),
    recipe_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id)
);

alter table recipes
    owner to demodb;

ALTER SEQUENCE recipes_recipe_id_seq
OWNED BY public.recipes.recipe_id;


-- public.menu_recipe sql table

CREATE SEQUENCE menu_recipe_menu_recipe_id_seq;

CREATE TABLE IF NOT EXISTS public.menu_recipe
(
    menu_recipe_id integer NOT NULL DEFAULT nextval('menu_recipe_menu_recipe_id_seq'),
    menu_id integer,
    recipe_id integer,
    CONSTRAINT menu_recipe_pkey PRIMARY KEY (menu_recipe_id),
    CONSTRAINT menu_recipe_menu_id_fkey FOREIGN KEY (menu_id)
        REFERENCES public.weekly_menu (menu_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT menu_recipe_recipe_id_fkey FOREIGN KEY (recipe_id)
        REFERENCES public.recipes (recipe_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

alter table menu_recipe
    owner to demodb;

ALTER SEQUENCE menu_recipe_menu_recipe_id_seq
OWNED BY public.menu_recipe.menu_recipe_id;

-- public.recipe_ingredient sql table

CREATE SEQUENCE recipe_ingredient_recipe_ingredient_id_seq;

CREATE TABLE IF NOT EXISTS public.recipe_ingredient
(
    recipe_ingredient_id integer NOT NULL DEFAULT nextval('recipe_ingredient_recipe_ingredient_id_seq'),
    recipe_id integer,
    ingredient_id integer,
    CONSTRAINT recipe_ingredient_pkey PRIMARY KEY (recipe_ingredient_id),
    CONSTRAINT recipe_ingredient_ingredient_id_fkey FOREIGN KEY (ingredient_id)
        REFERENCES public.ingredients (ingredient_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT recipe_ingredient_recipe_id_fkey FOREIGN KEY (recipe_id)
        REFERENCES public.recipes (recipe_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

alter table recipe_ingredient
    owner to demodb;

ALTER SEQUENCE recipe_ingredient_recipe_ingredient_id_seq
OWNED BY public.recipe_ingredient.recipe_ingredient_id;

insert into ingredients (ingredient_name) values('Garlic');
insert into ingredients (ingredient_name) values('Onion');
insert into ingredients (ingredient_name) values('Lemon');
insert into ingredients (ingredient_name) values('Tomato');
insert into ingredients (ingredient_name) values('Chilli');
insert into ingredients (ingredient_name) values('Broccoli');
insert into ingredients (ingredient_name) values('Salt');
insert into ingredients (ingredient_name) values('Paneer');

insert into recipes (recipe_name, description) values('Grilled Vegetable Salad', 'tossed vegetables with salt & pepper' );
insert into recipes (recipe_name, description) values('Italian Chopped Salad', 'Chopped vegetables with salt & pepper' );
insert into recipes (recipe_name, description) values('Pizza', 'cheese loaded Pizza' );
insert into recipes (recipe_name, description) values('Sandwich', 'tossed vegetables stuffed with cheese' );
insert into recipes (recipe_name, description) values('Pasta', 'Popular among all' );
insert into recipes (recipe_name, description) values('Coffee', 'Popular among all' );

insert into weekly_menu (menu_id, menu_name) values(1, 'week01');
insert into weekly_menu (menu_id, menu_name) values(2, 'week01');
insert into weekly_menu (menu_id, menu_name) values(3, 'week03');
insert into weekly_menu (menu_id, menu_name) values(5, 'week05');
insert into weekly_menu (menu_id, menu_name) values(6, 'week06');

insert into menu_recipe (menu_id, recipe_id) values(1, 1 );
insert into menu_recipe (menu_id, recipe_id) values(1, 2 );
insert into menu_recipe (menu_id, recipe_id) values(1, 3 );
insert into menu_recipe (menu_id, recipe_id) values(1, 4 );
insert into menu_recipe (menu_id, recipe_id) values(1, 5 );
insert into menu_recipe (menu_id, recipe_id) values(1, 6 );


insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 1 );
insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 2 );
insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 3 );
insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 4 );
insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 5 );
insert into recipe_ingredient (recipe_id, ingredient_id) values(1, 6 );