myStore.controller('myReviewsController', function(){
	this.reviews = {}

	this.addReview = function(product){

		if(!product.reviews)
			product.reviews =[]

		product.reviews.push(this.reviews)
		this.reviews = {}
	}
})