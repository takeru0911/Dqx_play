package controllers;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import models.Category;
import models.Item;
import models.MarketItem;
import models.RootCategory;
import play.libs.Json;
import play.mvc.Controller;
import play.mvc.Result;
import views.html.index;

public class Application extends Controller {
	private static List<Category> tempList;

	public static Result index() {
		return ok(index.render(RootCategory.all()));
	}
	public static Result category(){
		return ok(index.render(RootCategory.all()));
	}
	public static Result getItemByCategoryId(int id){
		List<Item> result = Item.findByCategoryId(new Long(id));

		return ok(Json.toJson(result));
	}
	public static Result getAllCategory(){
		List<Category> result = Category.all();
		Map<Integer, List<Category>> categoryMap = new HashMap<Integer, List<Category>>();
		IntStream.range(1, 5).forEach(index ->
		{
			categoryMap.put(index, result.stream()
					.filter(data->data.root_id == index)
					.collect(Collectors.toList()));
		});

		return ok(Json.toJson(categoryMap));
	}

	public static Result getItemMarketData(int id){
		List<MarketItem> result = MarketItem.findByCategoryId(new Long(id));
		Map<Integer, List<Long>> filteredByStar = new HashMap();
		IntStream.rangeClosed(0, 3).forEach(numOfStar ->
		{
			filteredByStar.put(numOfStar,result.stream()
				.filter(data -> data.stars == numOfStar)
				.map(data-> data.price)
				.collect(Collectors.toList()));
		});

		return ok(Json.toJson(filteredByStar));
	}
}
